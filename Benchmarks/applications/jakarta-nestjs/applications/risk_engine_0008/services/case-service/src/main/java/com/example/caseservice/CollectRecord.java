// SPDX-License-Identifier: Apache-2.0
package com.example.caseservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectRecord {


    @GET
    @Path("/CollectRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectRecord(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(synopsis, "http");
        String verdict = kv.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(verdict)) { return Response.status(403).build(); }
        String grievance = verdict;
        new ProcessBuilder(grievance).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
