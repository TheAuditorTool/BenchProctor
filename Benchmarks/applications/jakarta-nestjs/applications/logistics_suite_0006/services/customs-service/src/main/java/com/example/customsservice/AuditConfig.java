// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class AuditConfig {


    @GET
    @Path("/AuditConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditConfig(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(summary, "body");
        String consignment = tuple.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", consignment}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
