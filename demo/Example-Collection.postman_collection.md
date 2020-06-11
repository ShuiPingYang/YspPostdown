# Example-Collection

## An example collection for postdown.

*This example could show you what's the postdown could do.*

### 1.测试一下

```http
GET 0/get/example
```

> ### An example API.

You should write the detail about this API.

**It's markdown supported.**


#### Request

##### This's a right way to use.

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|

**Header**

|key|value|description|
|---|---|---|
|example-header|example-header-value|example-description|

**Response**

**Body**

```json
{
  "result": "successful"
}
```

#### Request

##### This's the worry way to use.

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|

**Header**

|key|value|description|
|---|---|---|
|example-header|example-header-value|example-description|

**Response**

**Body**

```json
{
  "result": "unsuccessful"
}
```

----------------

### 2.An example API with POST

```http
POST 0/post/example
```

> ### An example API.

You should write the detail about this API.

**It's markdown supported.**


#### Request

##### Successful Request

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|

**Header**

|key|value|description|
|---|---|---|
|example-header|example-header-value|example-description|

**Body**

|key|value|type|description|
|---|---|---|---|
|example-key|example-value|text|example-description|

**Response**

**Body**

```json
{
  "result": [
    "successful"
  ]
}
```

#### Request

##### Unsuccessful Requests

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|

**Header**

|key|value|description|
|---|---|---|
|example-header|example-header-value|example-description|

**Body**

|key|value|type|description|
|---|---|---|---|
|example-key|example-value|text|example-description|

**Response**

**Body**

```json
{
  "result": [
    "unsuccessful"
  ]
}
```

----------------

### 3.An example API with JSON

```http
POST 0/json/example
```

> ### An example API.

You should write the detail about this API.

**It's markdown supported.**


#### Request

##### Successful Request

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|

**Header**

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|
|Content-Type|application/json||

**Body**

```
{
	"example-key": "example-value"
}
```

**Response**

**Body**

```json
{
  "result": "successful"
}
```

#### Request

##### Unsuccessful Request

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|

**Header**

|key|value|description|
|---|---|---|
|example-key|example-value|example-description|
|Content-Type|application/json||

**Body**

```
{
	"example-key": "example-value"
}
```

**Response**

**Body**

```json
{
  "result": "unsuccessful"
}
```

----------------

