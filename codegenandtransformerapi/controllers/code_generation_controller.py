# -*- coding: utf-8 -*-

"""
    codegenandtransformerapi.controllers.code_generation_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..exceptions.api_exception import APIException

class CodeGenerationController(BaseController):

    """A Controller to access Endpoints in the codegenandtransformerapi API."""


    def using_file_as_string(self,
                             name,
                             format,
                             template,
                             body,
                             dl=0):
        """Does a POST request to /codegen.

        The code generation endpoint. The response is a path to the generated
        zip file relative to https://apimatic.io/

        Args:
            name (string): The name of the API being used for code generation
            format (Format): The format of the API description to use for code
                generation
            template (Template): The template to use for code generation
            body (string): The input file to use for code generation
            dl (int, optional): Optional

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'name': name,
            'format': format,
            'template': template,
            'dl': dl
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'body': body
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, files=_files)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized: Access is denied due to invalid credentials.', _context)
        elif _context.response.status_code == 412:
            raise APIException('Precondition Failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def using_url_as_string(self,
                            template,
                            format,
                            name,
                            description_url,
                            dl=0):
        """Does a GET request to /codegen.

        The code generation endpoint. The response is a path to the generated
        zip file relative to https://apimatic.io/

        Args:
            template (Template): The template to use for code generation
            format (Format): The format of the API description to use for code
                generation
            name (string): The name of the API being used for code generation
            description_url (string): The absolute public Uri for an API
                description doucment
            dl (int, optional): Optional

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'template': template,
            'format': format,
            'name': name,
            'descriptionUrl': description_url,
            'dl': dl
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized: Access is denied due to invalid credentials.', _context)
        elif _context.response.status_code == 412:
            raise APIException('Precondition Failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def using_file_as_binary(self,
                             name,
                             format,
                             template,
                             body,
                             dl=1):
        """Does a POST request to /codegen.

        The code generation endpoint! Upload a file and convert it to the
        given format. The API description format of uploaded file will be
        detected automatically. The response is generated zip file as per
        selected template.

        Args:
            name (string): The name of the API being used for code generation
            format (Format): The format of the API description to use for code
                generation
            template (Template): The template to use for code generation
            body (string): The input file to use for code generation
            dl (int, optional): Optional

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'name': name,
            'format': format,
            'template': template,
            'dl': dl
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'body': body
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, files=_files)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized: Access is denied due to invalid credentials.', _context)
        elif _context.response.status_code == 412:
            raise APIException('Precondition Failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def using_url_as_binary(self,
                            template,
                            format,
                            name,
                            description_url,
                            dl=1):
        """Does a GET request to /codegen.

        Download API description from the given URL and convert it to the
        given format. The API description format of the provided file will be
        detected automatically. The response is generated zip file as per
        selected template.

        Args:
            template (Template): The template to use for code generation
            format (Format): The format of the API description to use for code
                generation
            name (string): The name of the API being used for code generation
            description_url (string): The absolute public Uri for an API
                description doucment
            dl (int, optional): Optional

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'template': template,
            'format': format,
            'name': name,
            'descriptionUrl': description_url,
            'dl': dl
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized: Access is denied due to invalid credentials.', _context)
        elif _context.response.status_code == 412:
            raise APIException('Precondition Failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def using_apikey_as_binary(self,
                               apikey,
                               template,
                               dl=1):
        """Does a GET request to /codegen.

        Convert an API from the user's account using the API's [API
        Integration
        Key](https://docs.apimatic.io/getting-started/manage-apis/#view-api-int
        egration-key). The response is generated zip file as per selected
        template.
        > Note: This endpoint does not require Basic Authentication.

        Args:
            apikey (string): The API Key of the pre-configured API
            template (Template): The template to use for code generation
            dl (int, optional): Optional

        Returns:
            binary: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'apikey': apikey,
            'template': template,
            'dl': dl
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized: Access is denied due to invalid credentials.', _context)
        elif _context.response.status_code == 412:
            raise APIException('Precondition Failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def using_apikey_as_string(self,
                               apikey,
                               template,
                               dl=0):
        """Does a GET request to /codegen.

        The code generation endpoint. The response is a path to the generated
        zip file relative to https://apimatic.io/
        > Note: This endpoint does not require Basic Authentication.

        Args:
            apikey (string): The API Key of the pre-configured API
            template (Template): The template to use for code generation
            dl (int, optional): Optional

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'apikey': apikey,
            'template': template,
            'dl': dl
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized: Access is denied due to invalid credentials.', _context)
        elif _context.response.status_code == 412:
            raise APIException('Precondition Failed', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
