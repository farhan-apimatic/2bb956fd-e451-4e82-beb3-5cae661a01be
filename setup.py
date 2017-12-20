from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='codegenandtransformerapi',
    version='1.0.0',
    description='# APIMATIC CodeGen as a Service  [APIMATIC](https://apimatic.io) is an automatic code generator for RESTful APIs. This API exposes the access to its underlying code generation engine. We currently support the following format for API descriptions, `API Blueprint`, `RAML`, `Google API Discovery`, `IODocs`, `WADL`, and  `Swagger`. Although most API descriptions can be used, not all API decsriptions are written well-enough for automatic code generation and may fail the code generation process. For this purpose, we have provided a verbose validation API, which can be used to improve your API description.  > **Looking for a way to convert between API description formats like Swagger and API Blueprint?** Try [APIMATIC's Transformer API](http://docs.apimatictransformerapi.apiary.io/#) or it's web version at [Transformer](https://apimatic.io/transformer).  [APIMATIC](https://apimatic.io) works in two modes i.e., perform operations on **pre-configured** API descriptions, and perform  operations on API descriptions sent **on the fly** with requests. The later mode of operations has its limitations with respect to the customization of the generated code through our *codegen settings*.  See [this article](https://docs.apimatic.io/api-editor/codegen-settings/) for more information about customization of the output code.  ## Working with pre-configured API descriptions  This mode of operation is useful where APIs are stable and therefore can be pre-configured in [APIMATIC](https://apimatic.io). You can always update an API description in [APIMATIC](https://apimatic.io) using the API Editor by clicking on the *Edit* button. When working with stored API descriptions, pre-configured *codegen settings* are used that allow customization of the generated output. In order to uniquely identify the API to perform operations on, an *API Key* is used, which can be retrieved using the API context menu. This *API Key* is a secret value and therefore operations on pre-configured API descriptions do not require authentication.  See [this article](https://docs.apimatic.io/getting-started/manage-apis/#view-api-integration-key) on how to get your API Key from [APIMATIC](https://apimatic.io).  ## Working with API descriptions documents  This mode of operation is useful in cases where API descriptions are automatically generated from a process or external source and cannot be pre-configured in [APIMATIC](https://apimatic.io). In this case code generation uses the default *codegen settings*. However, if custom *codegen settings* are desired you may use the [APIMATIC](https://apimatic.io) format for generating your API descriptions, which contains nested *codegen settings*. For getting the full benefit of our advanced features in our code generator, you must either pre-configure your API, or use [APIMATIC](https://apimatic.io) format for API description.  # APIMATIC API Transformer  [APIMATIC](https://www.apimatic.io) Transformer allows its users to convert between different API description formats e.g. `Swagger`, `RAML`, etc. This enables the user to benefit from a wide range of tools available associated with any format, not just one.  The complete list of supported formats of [Transformer](https://apimatic.io/transformer) are:   Inputs     | Outputs ------------------  | ------------------- API Blueprint  | API Blueprint Swagger v.1.2  | Swagger 1.2 Swagger 2.0 (JSON and YAML) | Swagger 2.0 (JSON, YAML) Open API v.3.0  | Open API 3.0 WADL 2009 (W3C) | WADL 2009 (W3C) WSDL (W3C)  | WSDL (W3C) Google Discovery    | RAML 0.8 - 1.0  RAML 0.8 - 1.0     | Postman Collection 1.0 - 2.0 I/O Docs - Mashery | APIMATIC Format  HAR 1.2  | Postman Collection 1.0 - 2.0 | APIMATIC Format  | Mashape  |',
    long_description=long_description,
    author='APIMatic SDK Generator',
    author_email='support@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)