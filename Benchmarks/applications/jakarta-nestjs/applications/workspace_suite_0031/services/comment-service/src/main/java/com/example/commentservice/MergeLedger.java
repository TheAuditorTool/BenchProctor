// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class MergeLedger {


    @POST
    @Path("/MergeLedger")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeLedger(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(caption, "request");
        String synopsis = tuple.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(synopsis)) { return Response.status(403).build(); }
        String snippet = synopsis;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(snippet);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
