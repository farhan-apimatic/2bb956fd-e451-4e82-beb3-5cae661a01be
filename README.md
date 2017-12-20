# Getting started

# APIMATIC CodeGen as a Service

[APIMATIC](https://apimatic.io) is an automatic code generator for RESTful APIs. This API exposes the access to its underlying code
generation engine. We currently support the following format for API descriptions, `API Blueprint`, `RAML`,
`Google API Discovery`, `IODocs`, `WADL`, and  `Swagger`. Although most API descriptions can be used, not all API
decsriptions are written well-enough for automatic code generation and may fail the code generation process.
For this purpose, we have provided a verbose validation API, which can be used to improve your API description.

> **Looking for a way to convert between API description formats like Swagger and API Blueprint?** Try [APIMATIC's Transformer API](http://docs.apimatictransformerapi.apiary.io/#) or it's web version at [Transformer](https://apimatic.io/transformer).

[APIMATIC](https://apimatic.io) works in two modes i.e., perform operations on **pre-configured** API descriptions, and perform 
operations on API descriptions sent **on the fly** with requests. The later mode of operations has its
limitations with respect to the customization of the generated code through our *codegen settings*.

See [this article](https://docs.apimatic.io/api-editor/codegen-settings/)
for more information about customization of the output code.

## Working with pre-configured API descriptions

This mode of operation is useful where APIs are stable and therefore can be pre-configured in [APIMATIC](https://apimatic.io).
You can always update an API description in [APIMATIC](https://apimatic.io) using the API Editor by clicking on the *Edit* button.
When working with stored API descriptions, pre-configured *codegen settings* are used that allow customization
of the generated output. In order to uniquely identify the API to perform operations on, an *API Key* is used,
which can be retrieved using the API context menu. This *API Key* is a secret value and therefore operations
on pre-configured API descriptions do not require authentication.

See [this article](https://docs.apimatic.io/getting-started/manage-apis/#view-api-integration-key)
on how to get your API Key from [APIMATIC](https://apimatic.io).

## Working with API descriptions documents

This mode of operation is useful in cases where API descriptions are automatically generated from a process
or external source and cannot be pre-configured in [APIMATIC](https://apimatic.io). In this case code generation uses the default
*codegen settings*. However, if custom *codegen settings* are desired you may use the [APIMATIC](https://apimatic.io) format for
generating your API descriptions, which contains nested *codegen settings*. For getting the full benefit
of our advanced features in our code generator, you must either pre-configure your API, or use [APIMATIC](https://apimatic.io)
format for API description.

# APIMATIC API Transformer

[APIMATIC](https://www.apimatic.io) Transformer allows its users to convert between different API description formats e.g. `Swagger`, `RAML`, etc. This enables the user to benefit from a wide range of tools available associated with any format, not just one. 
The complete list of supported formats of [Transformer](https://apimatic.io/transformer) are: 

Inputs  			| Outputs
------------------  | -------------------
API Blueprint		| API Blueprint
Swagger v.1.2		| Swagger 1.2
Swagger 2.0 (JSON and YAML)	| Swagger 2.0 (JSON, YAML)
Open API v.3.0 	| Open API 3.0
WADL 2009 (W3C)	| WADL 2009 (W3C)
WSDL (W3C)		| WSDL (W3C)
Google Discovery    | RAML 0.8 - 1.0	
RAML 0.8 - 1.0	    | Postman Collection 1.0 - 2.0
I/O Docs - Mashery	| APIMATIC Format	
HAR 1.2		|
Postman Collection 1.0 - 2.0	|
APIMATIC Format		|
Mashape		|

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=CodeGen%20and%20Transformer%20API-Python)


## How to Use

The following section explains how to use the Codegenandtransformerapi SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=CodeGen%20and%20Transformer%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=CodeGen%20and%20Transformer%20API-Python&projectName=codegenandtransformerapi)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=CodeGen%20and%20Transformer%20API-Python&projectName=codegenandtransformerapi)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=CodeGen%20and%20Transformer%20API-Python&projectName=codegenandtransformerapi)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from codegenandtransformerapi.codegenandtransformerapi_client import CodegenandtransformerapiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=CodeGen%20and%20Transformer%20API-Python&libraryName=codegenandtransformerapi.codegenandtransformerapi_client&projectName=codegenandtransformerapi&className=CodegenandtransformerapiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=CodeGen%20and%20Transformer%20API-Python&libraryName=codegenandtransformerapi.codegenandtransformerapi_client&projectName=codegenandtransformerapi&className=CodegenandtransformerapiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = CodegenandtransformerapiClient(basic_auth_user_name, basic_auth_password)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [CodeGenerationController](#code_generation_controller)
* [APIDescriptionValidationController](#api_description_validation_controller)
* [APITransformerController](#api_transformer_controller)

## <a name="code_generation_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CodeGenerationController") CodeGenerationController

### Get controller instance

An instance of the ``` CodeGenerationController ``` class can be accessed from the API Client.

```python
 code_generation_controller = client.code_generation
```

### <a name="using_file_as_string"></a>![Method: ](https://apidocs.io/img/method.png ".CodeGenerationController.using_file_as_string") using_file_as_string

> The code generation endpoint. The response is a path to the generated zip file relative to https://apimatic.io/

```python
def using_file_as_string(self,
                             name,
                             format,
                             template,
                             body,
                             dl=0)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Required ```  | The name of the API being used for code generation |
| format |  ``` Required ```  | The format of the API description to use for code generation |
| template |  ``` Required ```  | The template to use for code generation |
| body |  ``` Required ```  | The input file to use for code generation |
| dl |  ``` Optional ```  ``` DefaultValue ```  | Optional |



#### Example Usage

```python
name = 'name'
format = Format.ENUM_API BLUEPRINT
template = Template.CS_PORTABLE_NET_LIB
body = open("pathtofile", 'rb')
dl = 0

result = code_generation_controller.using_file_as_string(name, format, template, body, dl)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized: Access is denied due to invalid credentials. |
| 412 | Precondition Failed |




### <a name="using_url_as_string"></a>![Method: ](https://apidocs.io/img/method.png ".CodeGenerationController.using_url_as_string") using_url_as_string

> The code generation endpoint. The response is a path to the generated zip file relative to https://apimatic.io/

```python
def using_url_as_string(self,
                            template,
                            format,
                            name,
                            description_url,
                            dl=0)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| template |  ``` Required ```  | The template to use for code generation |
| format |  ``` Required ```  | The format of the API description to use for code generation |
| name |  ``` Required ```  | The name of the API being used for code generation |
| descriptionUrl |  ``` Required ```  | The absolute public Uri for an API description doucment |
| dl |  ``` Optional ```  ``` DefaultValue ```  | Optional |



#### Example Usage

```python
template = Template.CS_PORTABLE_NET_LIB
format = Format.ENUM_API BLUEPRINT
name = 'name'
description_url = 'descriptionUrl'
dl = 0

result = code_generation_controller.using_url_as_string(template, format, name, description_url, dl)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized: Access is denied due to invalid credentials. |
| 412 | Precondition Failed |




### <a name="using_file_as_binary"></a>![Method: ](https://apidocs.io/img/method.png ".CodeGenerationController.using_file_as_binary") using_file_as_binary

> The code generation endpoint! Upload a file and convert it to the given format. The API description format of uploaded file will be detected automatically. The response is generated zip file as per selected template.

```python
def using_file_as_binary(self,
                             name,
                             format,
                             template,
                             body,
                             dl=1)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| name |  ``` Required ```  | The name of the API being used for code generation |
| format |  ``` Required ```  | The format of the API description to use for code generation |
| template |  ``` Required ```  | The template to use for code generation |
| body |  ``` Required ```  | The input file to use for code generation |
| dl |  ``` Optional ```  ``` DefaultValue ```  | Optional |



#### Example Usage

```python
name = 'name'
format = Format.ENUM_API BLUEPRINT
template = Template.CS_PORTABLE_NET_LIB
body = open("pathtofile", 'rb')
dl = 1

result = code_generation_controller.using_file_as_binary(name, format, template, body, dl)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized: Access is denied due to invalid credentials. |
| 412 | Precondition Failed |




### <a name="using_url_as_binary"></a>![Method: ](https://apidocs.io/img/method.png ".CodeGenerationController.using_url_as_binary") using_url_as_binary

> Download API description from the given URL and convert it to the given format. The API description format of the provided file will be detected automatically. The response is generated zip file as per selected template.

```python
def using_url_as_binary(self,
                            template,
                            format,
                            name,
                            description_url,
                            dl=1)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| template |  ``` Required ```  | The template to use for code generation |
| format |  ``` Required ```  | The format of the API description to use for code generation |
| name |  ``` Required ```  | The name of the API being used for code generation |
| descriptionUrl |  ``` Required ```  | The absolute public Uri for an API description doucment |
| dl |  ``` Optional ```  ``` DefaultValue ```  | Optional |



#### Example Usage

```python
template = Template.CS_PORTABLE_NET_LIB
format = Format.ENUM_API BLUEPRINT
name = 'name'
description_url = 'descriptionUrl'
dl = 1

result = code_generation_controller.using_url_as_binary(template, format, name, description_url, dl)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized: Access is denied due to invalid credentials. |
| 412 | Precondition Failed |




### <a name="using_apikey_as_binary"></a>![Method: ](https://apidocs.io/img/method.png ".CodeGenerationController.using_apikey_as_binary") using_apikey_as_binary

> Convert an API from the user's account using the API's [API Integration Key](https://docs.apimatic.io/getting-started/manage-apis/#view-api-integration-key). The response is generated zip file as per selected template.
> > Note: This endpoint does not require Basic Authentication.

```python
def using_apikey_as_binary(self,
                               apikey,
                               template,
                               dl=1)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| apikey |  ``` Required ```  | The API Key of the pre-configured API |
| template |  ``` Required ```  | The template to use for code generation |
| dl |  ``` Optional ```  ``` DefaultValue ```  | Optional |



#### Example Usage

```python
apikey = 'apikey'
template = Template.CS_PORTABLE_NET_LIB
dl = 1

result = code_generation_controller.using_apikey_as_binary(apikey, template, dl)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized: Access is denied due to invalid credentials. |
| 412 | Precondition Failed |




### <a name="using_apikey_as_string"></a>![Method: ](https://apidocs.io/img/method.png ".CodeGenerationController.using_apikey_as_string") using_apikey_as_string

> The code generation endpoint. The response is a path to the generated zip file relative to https://apimatic.io/
> > Note: This endpoint does not require Basic Authentication.

```python
def using_apikey_as_string(self,
                               apikey,
                               template,
                               dl=0)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| apikey |  ``` Required ```  | The API Key of the pre-configured API |
| template |  ``` Required ```  | The template to use for code generation |
| dl |  ``` Optional ```  ``` DefaultValue ```  | Optional |



#### Example Usage

```python
apikey = 'apikey'
template = Template.CS_PORTABLE_NET_LIB
dl = 0

result = code_generation_controller.using_apikey_as_string(apikey, template, dl)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized: Access is denied due to invalid credentials. |
| 412 | Precondition Failed |




[Back to List of Controllers](#list_of_controllers)

## <a name="api_description_validation_controller"></a>![Class: ](https://apidocs.io/img/class.png ".APIDescriptionValidationController") APIDescriptionValidationController

### Get controller instance

An instance of the ``` APIDescriptionValidationController ``` class can be accessed from the API Client.

```python
 api_description_validation_controller = client.api_description_validation
```

### <a name="using_file"></a>![Method: ](https://apidocs.io/img/method.png ".APIDescriptionValidationController.using_file") using_file

> This endpoint can be used to validate an API description document *on the fly* and see detailed error messages along with any warnings or useful information.

```python
def using_file(self,
                   body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | The input file to use for validation |



#### Example Usage

```python
body = open("pathtofile", 'rb')

result = api_description_validation_controller.using_file(body)

```


### <a name="using_url"></a>![Method: ](https://apidocs.io/img/method.png ".APIDescriptionValidationController.using_url") using_url

> This endpoint can be used to validate an API description document *on the fly* from its public Uri, and see detailed error messages along with any warnings or useful information. This endpoint is useful for API descriptions with relative links e.g., includes (RAML) and paths (swagger).

```python
def using_url(self,
                  description_url)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| descriptionUrl |  ``` Required ```  | The absolute public Uri for an API description doucment |



#### Example Usage

```python
description_url = 'descriptionUrl'

result = api_description_validation_controller.using_url(description_url)

```


### <a name="using_apikey"></a>![Method: ](https://apidocs.io/img/method.png ".APIDescriptionValidationController.using_apikey") using_apikey

> This endpoint can be used to validate a *pre-configured* API description and see detailed error messages along with any warnings or useful information.

```python
def using_apikey(self,
                     apikey)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| apikey |  ``` Required ```  | The API Key of a pre-configured API description from APIMATIC |



#### Example Usage

```python
apikey = 'apikey'

result = api_description_validation_controller.using_apikey(apikey)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="api_transformer_controller"></a>![Class: ](https://apidocs.io/img/class.png ".APITransformerController") APITransformerController

### Get controller instance

An instance of the ``` APITransformerController ``` class can be accessed from the API Client.

```python
 api_transformer_controller = client.api_transformer
```

### <a name="using_apikey"></a>![Method: ](https://apidocs.io/img/method.png ".APITransformerController.using_apikey") using_apikey

> Convert an API from the user's account using the API's [Api Integration Key](https://docs.apimatic.io/getting-started/manage-apis/#view-api-integration-key). The converted file is returned as the response.
> > Note: This endpoint does not require Basic Authentication.

```python
def using_apikey(self,
                     format,
                     apikey)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| format |  ``` Required ```  | The API format to convert to |
| apikey |  ``` Required ```  | Apikey of an already uploaded API Description on APIMATIC |



#### Example Usage

```python
format = FormatTransformer.APIMATIC
apikey = 'apikey'

result = api_transformer_controller.using_apikey(format, apikey)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |




### <a name="using_url"></a>![Method: ](https://apidocs.io/img/method.png ".APITransformerController.using_url") using_url

> Download API description from the given URL and convert it to the given format. The API description format of the provided file will be detected automatically. The converted file is returned as the response.

```python
def using_url(self,
                  format,
                  description_url)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| format |  ``` Required ```  | The API format to convert to |
| descriptionUrl |  ``` Required ```  | The URL where the API description will be downloaded from |



#### Example Usage

```python
format = FormatTransformer.APIMATIC
description_url = 'descriptionUrl'

result = api_transformer_controller.using_url(format, description_url)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |




### <a name="using_file"></a>![Method: ](https://apidocs.io/img/method.png ".APITransformerController.using_file") using_file

> Upload a file and convert it to the given format. The API description format of the uploaded file will be detected automatically. The converted file is returned as the response.

```python
def using_file(self,
                   format,
                   file)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| format |  ``` Required ```  | The API format to convert to |
| file |  ``` Required ```  | The input file to convert |



#### Example Usage

```python
format = FormatTransformer.APIMATIC
file = open("pathtofile", 'rb')

result = api_transformer_controller.using_file(format, file)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |




[Back to List of Controllers](#list_of_controllers)



