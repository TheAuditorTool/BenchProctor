// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class SummarizeRecord {


    @GET
    @Path("/SummarizeRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeRecord(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(remark, "header");
        String synopsis = tuple.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(synopsis)) { return Response.status(403).build(); }
        String quotation = synopsis;
        new ProcessBuilder(quotation).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
