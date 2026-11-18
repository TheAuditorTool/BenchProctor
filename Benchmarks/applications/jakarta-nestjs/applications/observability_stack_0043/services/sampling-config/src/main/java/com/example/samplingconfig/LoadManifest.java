// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class LoadManifest {


    @GET
    @Path("/LoadManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadManifest(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(note, "query");
        String gauge = kv.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(gauge)) { return Response.status(403).build(); }
        String cohort = gauge;
        new ProcessBuilder(cohort).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
