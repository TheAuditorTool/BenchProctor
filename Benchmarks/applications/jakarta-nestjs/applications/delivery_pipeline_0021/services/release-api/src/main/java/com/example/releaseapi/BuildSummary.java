// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class BuildSummary {


    @GET
    @Path("/BuildSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildSummary(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : summary.split(",")) { tokens.add(token.trim()); }
        String phrase = String.join(",", tokens);
        String subtitle = phrase.matches("^(status|info|list|show)$") ? phrase : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + subtitle}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
