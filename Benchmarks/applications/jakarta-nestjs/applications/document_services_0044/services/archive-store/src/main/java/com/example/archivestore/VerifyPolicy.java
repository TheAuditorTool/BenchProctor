// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class VerifyPolicy {


    @GET
    @Path("/VerifyPolicy")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyPolicy(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : phrase.split(",")) { tokens.add(token.trim()); }
        String dossier = String.join(",", tokens);
        String addendum = dossier.matches("^(status|info|list|show)$") ? dossier : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + addendum}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
