// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class BuildPayout {


    @POST
    @Path("/BuildPayout")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildPayout(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(footnote, "request");
        String remittance = entry.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(remittance)) { return Response.status(403).build(); }
        String disbursement = remittance;
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command(disbursement);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
