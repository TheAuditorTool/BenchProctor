// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class ValidateSummary {


    @GET
    @Path("/ValidateSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateSummary(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : caption.split(",")) { tokens.add(token.trim()); }
        String remittance = String.join(",", tokens);
        String dunning = remittance.matches("^(status|info|list|show)$") ? remittance : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + dunning}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
