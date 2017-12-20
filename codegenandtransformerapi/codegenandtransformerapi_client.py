# -*- coding: utf-8 -*-

"""
    codegenandtransformerapi.code_gen_and_transformer_api_client

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .configuration import Configuration
from .controllers.code_generation_controller import CodeGenerationController
from .controllers.api_description_validation_controller import APIDescriptionValidationController
from .controllers.api_transformer_controller import APITransformerController

class CodegenandtransformerapiClient(object):

    config = Configuration

    @lazy_property
    def code_generation(self):
        return CodeGenerationController()

    @lazy_property
    def api_description_validation(self):
        return APIDescriptionValidationController()

    @lazy_property
    def api_transformer(self):
        return APITransformerController()


    def __init__(self, 
                 basic_auth_user_name = None,
                 basic_auth_password = None):
        if basic_auth_user_name != None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password != None:
            Configuration.basic_auth_password = basic_auth_password


