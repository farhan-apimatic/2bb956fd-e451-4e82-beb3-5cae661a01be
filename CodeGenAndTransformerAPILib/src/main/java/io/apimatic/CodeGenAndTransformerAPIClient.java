/*
 * CodeGenAndTransformerAPILib
 *
 * This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
 */
package io.apimatic;

import io.apimatic.controllers.*;
import io.apimatic.http.client.HttpClient;

public class CodeGenAndTransformerAPIClient {
    /**
     * Singleton access to CodeGeneration controller
     * @return	Returns the CodeGenerationController instance 
     */
    public CodeGenerationController getCodeGeneration() {
        return CodeGenerationController.getInstance();
    }

    /**
     * Singleton access to APIDescriptionValidation controller
     * @return	Returns the APIDescriptionValidationController instance 
     */
    public APIDescriptionValidationController getAPIDescriptionValidation() {
        return APIDescriptionValidationController.getInstance();
    }

    /**
     * Singleton access to APITransformer controller
     * @return	Returns the APITransformerController instance 
     */
    public APITransformerController getAPITransformer() {
        return APITransformerController.getInstance();
    }

    /**
     * Get the shared http client currently being used for API calls
     * @return The http client instance currently being used
     */
    public HttpClient getSharedHttpClient() {
        return BaseController.getClientInstance();
    }
    
    /**
     * Set a shared http client to be used for API calls
     * @param httpClient The http client to use
     */
    public void setSharedHttpClient(HttpClient httpClient) {
        BaseController.setClientInstance(httpClient);
    }

    /**
     * Default constructor 
     */     
    public CodeGenAndTransformerAPIClient() {
    }

    /**
     * Client initialization constructor 
     */     
    public CodeGenAndTransformerAPIClient(String basicAuthUserName, String basicAuthPassword) {
        this();
        Configuration.basicAuthUserName = basicAuthUserName;
        Configuration.basicAuthPassword = basicAuthPassword;
    }
}