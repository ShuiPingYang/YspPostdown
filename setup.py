from setuptools import setup
from ysp_postdown import __version__, __author__

setup(
    name='ysp_postdown',
    version=__version__,
    author=__author__,
    author_email='18611370423@qq.com',
    packages=['ysp_postdown'],
    package_data={
        'ysp_postdown': ['README.rst', 'LICENSE']
    },
    entry_points={'console_scripts': ['ysp_postdown = ysp_postdown.cmdline:execute']},
    url='https://github.com/ShuiPingYang/YspPostdown',
    description='Generate markdown API document from Postman.',
    long_description_content_type="text/markdown",
    long_description=open('README.rst').read(),
)
