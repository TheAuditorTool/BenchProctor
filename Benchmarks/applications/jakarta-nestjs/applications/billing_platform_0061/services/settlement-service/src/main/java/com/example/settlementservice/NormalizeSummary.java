// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class NormalizeSummary {


    @GET
    @Path("/NormalizeSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeSummary(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : footnote.split(",")) { tokens.add(token.trim()); }
        String remittance = String.join(",", tokens);
        String arrears = remittance.matches("^(status|info|list|show)$") ? remittance : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + arrears}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
