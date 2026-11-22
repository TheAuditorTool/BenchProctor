// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class AnnotateSchedule {


    @POST
    @Path("/AnnotateSchedule")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateSchedule(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(snippet, "request");
        String montage = kv.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(montage)) { return Response.status(403).build(); }
        String rendition = montage;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(rendition);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
