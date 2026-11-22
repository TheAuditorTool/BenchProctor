// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class ResolveTicket {


    @GET
    @Path("/ResolveTicket")
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveTicket(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String inquiry = String.join(",", tokens);
        String grievance = inquiry.matches("^(status|info|list|show)$") ? inquiry : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + grievance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
