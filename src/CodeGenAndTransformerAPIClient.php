<?php
/*
 * CodeGenAndTransformerAPILib
 *
 * This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
 */

namespace CodeGenAndTransformerAPILib;

use CodeGenAndTransformerAPILib\Controllers;

/**
 * CodeGenAndTransformerAPILib client class
 */
class CodeGenAndTransformerAPIClient
{
    /**
     * Constructor with authentication and configuration parameters
     */
    public function __construct(
        $basicAuthUserName = null,
        $basicAuthPassword = null
    ) {
        Configuration::$basicAuthUserName = $basicAuthUserName ? $basicAuthUserName : Configuration::$basicAuthUserName;
        Configuration::$basicAuthPassword = $basicAuthPassword ? $basicAuthPassword : Configuration::$basicAuthPassword;
    }
    /**
     * Singleton access to CodeGeneration controller
     * @return Controllers\CodeGenerationController The *Singleton* instance
     */
    public function getCodeGeneration()
    {
        return Controllers\CodeGenerationController::getInstance();
    }
    /**
     * Singleton access to APIDescriptionValidation controller
     * @return Controllers\APIDescriptionValidationController The *Singleton* instance
     */
    public function getAPIDescriptionValidation()
    {
        return Controllers\APIDescriptionValidationController::getInstance();
    }
    /**
     * Singleton access to APITransformer controller
     * @return Controllers\APITransformerController The *Singleton* instance
     */
    public function getAPITransformer()
    {
        return Controllers\APITransformerController::getInstance();
    }
}