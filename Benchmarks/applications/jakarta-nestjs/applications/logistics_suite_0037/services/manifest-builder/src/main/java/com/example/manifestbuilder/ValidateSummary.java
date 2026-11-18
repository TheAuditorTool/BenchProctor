// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ValidateSummary {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/ValidateSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateSummary(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(System.getenv("SHIPPING_INPUT_0037")).orElse("");
        String consignment = normalize(footnote);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + consignment}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
