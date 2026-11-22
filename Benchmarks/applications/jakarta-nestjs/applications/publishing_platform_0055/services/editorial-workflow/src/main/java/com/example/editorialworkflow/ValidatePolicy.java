// SPDX-License-Identifier: Apache-2.0
package com.example.editorialworkflow;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ValidatePolicy {


    @POST
    @Path("/ValidatePolicy")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validatePolicy(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(synopsis, "request");
        String byline = pair.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(byline)) { return Response.status(403).build(); }
        String addendum = byline;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(addendum);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
