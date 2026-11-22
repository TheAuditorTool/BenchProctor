// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class PruneCheckpoint {


    @GET
    @Path("/PruneCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : citation.split(",")) { tokens.add(token.trim()); }
        String rendition = String.join(",", tokens);
        String montage = rendition.matches("^(status|info|list|show)$") ? rendition : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + montage}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
