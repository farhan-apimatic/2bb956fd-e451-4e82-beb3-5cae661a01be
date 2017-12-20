/*
 * CodeGenAndTransformerAPILib
 *
 * This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
 */
package io.apimatic.exceptions;

import java.util.*;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonSetter;
import io.apimatic.http.client.HttpContext;
import io.apimatic.models.*;

public class ValidationResultException 
        extends APIException
        implements java.io.Serializable {
    private static final long serialVersionUID = 4816943153430018780L;
    private boolean success;
    private List<Message> errors;
    private List<Message> warnings;
    private List<Message> messages;
    /** GETTER
     * TODO: Write general description for this method
     */
    @JsonGetter("Success")
    public boolean getSuccess ( ) { 
        return this.success;
    }
    
    /** SETTER
     * TODO: Write general description for this method
     */
    @JsonSetter("Success")
    private void setSuccess (boolean value) { 
        this.success = value;
    }
 
    /** GETTER
     * TODO: Write general description for this method
     */
    @JsonGetter("Errors")
    public List<Message> getErrors ( ) { 
        return this.errors;
    }
    
    /** SETTER
     * TODO: Write general description for this method
     */
    @JsonSetter("Errors")
    private void setErrors (List<Message> value) { 
        this.errors = value;
    }
 
    /** GETTER
     * TODO: Write general description for this method
     */
    @JsonGetter("Warnings")
    public List<Message> getWarnings ( ) { 
        return this.warnings;
    }
    
    /** SETTER
     * TODO: Write general description for this method
     */
    @JsonSetter("Warnings")
    private void setWarnings (List<Message> value) { 
        this.warnings = value;
    }
 
    /** GETTER
     * TODO: Write general description for this method
     */
    @JsonGetter("Messages")
    public List<Message> getMessages ( ) { 
        return this.messages;
    }
    
    /** SETTER
     * TODO: Write general description for this method
     */
    @JsonSetter("Messages")
    private void setMessages (List<Message> value) { 
        this.messages = value;
    }
 
    /**
     * Initialization constructor
     * @param   reason  The reason for throwing exception
     * @param   context The http context of the API exception
     */
    public ValidationResultException(String reason, HttpContext context) {
        super(reason, context);
    }
}
 