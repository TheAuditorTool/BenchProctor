// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;

@Path("/")
class SummarizeHeader {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/SummarizeHeader")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeHeader(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = req.payload;
        String remittance;
        if (remark.length() > 256) { remittance = remark.substring(0, 256); }
        else { remittance = remark; }
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(remittance)).isEmpty()) { return Response.status(400).entity("schema invalid").build(); }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + remittance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
