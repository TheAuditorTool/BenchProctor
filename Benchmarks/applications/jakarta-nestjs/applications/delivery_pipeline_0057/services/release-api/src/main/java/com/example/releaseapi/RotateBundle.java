// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RotateBundle {


    @GET
    @Path("/RotateBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateBundle(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(footnote, "json");
        String wording = entry.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(wording)) { return Response.status(403).build(); }
        String note = wording;
        new ProcessBuilder(note).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
