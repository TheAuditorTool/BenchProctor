// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class EnrichCheckpoint {


    @GET
    @Path("/EnrichCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(footnote, "json");
        String handshake = pair.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(handshake)) { return Response.status(403).build(); }
        String blurb = handshake;
        new ProcessBuilder(blurb).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
