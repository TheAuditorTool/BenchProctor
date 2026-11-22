// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ArchiveSurvey {


    @POST
    @Path("/ArchiveSurvey")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveSurvey(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(preface, "query");
        String grievance = tuple.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(grievance)) { return Response.status(403).build(); }
        String inquiry = grievance;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(inquiry);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
