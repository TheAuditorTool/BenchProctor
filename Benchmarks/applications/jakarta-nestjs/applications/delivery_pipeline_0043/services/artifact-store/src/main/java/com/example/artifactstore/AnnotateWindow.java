// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class AnnotateWindow {


    @GET
    @Path("/AnnotateWindow")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateWindow(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String note = String.join(",", tokens);
        String phrase = note.matches("^(status|info|list|show)$") ? note : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + phrase}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
