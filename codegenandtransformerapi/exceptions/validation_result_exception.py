# -*- coding: utf-8 -*-

"""
    codegenandtransformerapi.models.validation_result_exception

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from ..api_helper import APIHelper
import codegenandtransformerapi.exceptions.api_exception
import codegenandtransformerapi.models.message

class ValidationResultException(codegenandtransformerapi.exceptions.api_exception.APIException):
    def __init__(self, reason, context):
        """Constructor for the ValidationResultException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            context (HttpContext):  The HttpContext of the API call.

        """
        super(ValidationResultException, self).__init__(reason, context)
        dictionary = APIHelper.json_deserialize(self.context.response.raw_body)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.success = dictionary.get("Success")
        self.errors = None
        if dictionary.get("Errors") != None:
            self.errors = list()
            for structure in dictionary.get("Errors"):
                self.errors.append(codegenandtransformerapi.models.message.Message.from_dictionary(structure))
        self.warnings = None
        if dictionary.get("Warnings") != None:
            self.warnings = list()
            for structure in dictionary.get("Warnings"):
                self.warnings.append(codegenandtransformerapi.models.message.Message.from_dictionary(structure))
        self.messages = None
        if dictionary.get("Messages") != None:
            self.messages = list()
            for structure in dictionary.get("Messages"):
                self.messages.append(codegenandtransformerapi.models.message.Message.from_dictionary(structure))
