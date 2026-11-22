// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class ResolveRoster {


    @POST
    @Path("/ResolveRoster")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveRoster(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(preface, "form");
        String addendum = tuple.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(addendum)) { return Response.status(403).build(); }
        String dossier = addendum;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(dossier);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
