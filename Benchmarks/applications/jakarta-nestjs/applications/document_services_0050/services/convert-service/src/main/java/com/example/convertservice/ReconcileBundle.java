// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ReconcileBundle {


    @GET
    @Path("/ReconcileBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileBundle(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : citation.split(",")) { tokens.add(token.trim()); }
        String dossier = String.join(",", tokens);
        String addendum = dossier.matches("^(status|info|list|show)$") ? dossier : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + addendum}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
