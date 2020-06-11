import json
from .ctor import MDDoc


def get_rows(raw, keys):
    result = list()
    for i in raw:
        if i.get('key', ''):
            result.append([i.get(k, '') for k in keys])
    return result


def parse(in_file, out_file):
    doc = MDDoc()

    with open(in_file,'r',encoding='UTF-8') as f:
        collection = json.load(f)

    # The basic info.
    doc.title(collection['info']['name'])
    doc.line(collection['info'].get('description', ''))
    doc.br()

    # API
    for index,api in enumerate(collection['item']):
        doc.title(str(index+1) + '.' + api['name'], 3)
        request = api['request']
        url = request['url']['host'][0] +'/' + '/'.join(request['url']['path'])
        doc.code_block(
            '{0} {1}'.format(request['method'], url), 
            'http'
        )
        doc.description(request.get('description',''))

        if api['response']:
            # Response example.
            for response in api['response']:
                doc.comment_begin()

                # Request Query
                doc.bold('Request')
                if request['url'].get('query',''):
                    if isinstance(request['url'], dict):
                        rows = get_rows(
                            request['url']['query'],
                            ['key', 'value', 'description']
                        )
                        doc.table(['key', 'value', 'description'], rows)

                # Request Header
                if request['header']:
                    doc.bold('Header')
                    rows = get_rows(
                        request['header'],
                        ['key', 'value', 'description']
                    )
                    doc.table(['key', 'value', 'description'], rows)

                # Request Body
                if request.get('body',''):
                    content = request['body'][request['body']['mode']]
                    if request['body']['mode'] == 'file' and \
                            isinstance(content, dict):
                        content = content.get('src', '')

                    if content:
                        doc.bold('Body')
                        if request['body']['mode'] in ['formdata', 'urlencoded']:
                            rows = get_rows(
                                content,
                                ['key', 'value', 'type', 'description']
                            )
                            doc.table(
                                ['key', 'value', 'type', 'description'], rows
                            )
                        elif request['body']['mode'] == 'raw':
                            doc.code_block(request['body']['raw'])
                        elif request['body']['mode'] == 'file':
                            doc.text(request['body']['file']['src'])
                # Response
                doc.bold('Response')
                doc.bold('Body')
                doc.code_block(json.dumps(json.loads(response['body']), indent=2, ensure_ascii=False), 'json')
                doc.comment_end()

        else:
            # Request information.
            doc.title('Request', 4)

            # Request Header
            if request.get('header', '') and request['header'][0]['key']:
                doc.bold('Header')
                rows = get_rows(
                    request['header'],
                    ['key', 'value', 'description']
                )
                doc.table(['key', 'value', 'description'], rows)

            # Request Body
            if request.get('body',''):
                content = request['body'][request['body']['mode']]
                if request['body']['mode'] == 'file' and isinstance(content, dict):
                    content = content.get('src', '')

                if content:
                    doc.bold('Body')
                    if request['body']['mode'] in ['formdata', 'urlencoded']:
                        rows = get_rows(
                            request['body'][request['body']['mode']],
                            ['key', 'value', 'type', 'description']
                        )
                        doc.table(['key', 'value', 'type', 'description'], rows)
                    elif request['body']['mode'] == 'raw':
                        doc.code_block(request['body']['raw'], 'json')
                    elif request['body']['mode'] == 'file':
                        doc.text(request['body']['file']['src'])
        doc.hr()

    with open(out_file, 'w+',encoding="utf-8") as f:
        f.write(doc.output())

