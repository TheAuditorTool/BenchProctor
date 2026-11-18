// SPDX-License-Identifier: Apache-2.0
package com.example.tracecollector;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RotateTrace {


    @GET
    @Path("/RotateTrace")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateTrace(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(caption, "request");
        String cohort = edge.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(cohort)) { return Response.status(403).build(); }
        String gauge = cohort;
        new ProcessBuilder(gauge).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
