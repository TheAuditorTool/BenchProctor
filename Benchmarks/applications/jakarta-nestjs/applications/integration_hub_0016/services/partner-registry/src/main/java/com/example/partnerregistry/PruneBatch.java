// SPDX-License-Identifier: Apache-2.0
package com.example.partnerregistry;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class PruneBatch {


    @POST
    @Path("/PruneBatch")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneBatch(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(wording, "http");
        String handshake = tuple.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(handshake)) { return Response.status(403).build(); }
        String subject = handshake;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(subject);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
