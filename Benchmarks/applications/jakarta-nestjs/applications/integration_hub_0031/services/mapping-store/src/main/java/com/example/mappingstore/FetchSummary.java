// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@Path("/")
class FetchSummary {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/FetchSummary")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchSummary(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = req.payload;
        String handshake;
        if (snippet.length() > 256) { handshake = snippet.substring(0, 256); }
        else { handshake = snippet; }
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(handshake)).isEmpty()) { return Response.status(400).entity("schema invalid").build(); }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + handshake}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
