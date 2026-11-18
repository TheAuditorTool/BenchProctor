// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectProfile {


    @GET
    @Path("/CollectProfile")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectProfile(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(notice, "json");
        String persona = edge.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(persona)) { return Response.status(403).build(); }
        String handshake = persona;
        new ProcessBuilder(handshake).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
