# -*- coding: utf-8 -*-

"""
    codegenandtransformerapi.controllers.api_description_validation_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.validate_an_api_description_response import ValidateAnAPIDescriptionResponse

class APIDescriptionValidationController(BaseController):

    """A Controller to access Endpoints in the codegenandtransformerapi API."""


    def using_file(self,
                   body):
        """Does a POST request to /validate.

        This endpoint can be used to validate an API description document *on
        the fly* and see detailed error messages along with any warnings or
        useful information.

        Args:
            body (string): The input file to use for validation

        Returns:
            ValidateAnAPIDescriptionResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/validate'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'body': body
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, files=_files)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ValidateAnAPIDescriptionResponse.from_dictionary)

    def using_url(self,
                  description_url):
        """Does a GET request to /validate.

        This endpoint can be used to validate an API description document *on
        the fly* from its public Uri, and see detailed error messages along
        with any warnings or useful information. This endpoint is useful for
        API descriptions with relative links e.g., includes (RAML) and paths
        (swagger).

        Args:
            description_url (string): The absolute public Uri for an API
                description doucment

        Returns:
            ValidateAnAPIDescriptionResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/validate'
        _query_parameters = {
            'descriptionUrl': description_url
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ValidateAnAPIDescriptionResponse.from_dictionary)

    def using_apikey(self,
                     apikey):
        """Does a GET request to /validate.

        This endpoint can be used to validate a *pre-configured* API
        description and see detailed error messages along with any warnings or
        useful information.

        Args:
            apikey (string): The API Key of a pre-configured API description
                from APIMATIC

        Returns:
            ValidateAnAPIDescriptionResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/validate'
        _query_parameters = {
            'apikey': apikey
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ValidateAnAPIDescriptionResponse.from_dictionary)
