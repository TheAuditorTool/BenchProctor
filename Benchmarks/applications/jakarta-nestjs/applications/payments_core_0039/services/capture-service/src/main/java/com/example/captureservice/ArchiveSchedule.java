// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class ArchiveSchedule {


    @GET
    @Path("/ArchiveSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveSchedule(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : memo.split(",")) { tokens.add(token.trim()); }
        String ledger = String.join(",", tokens);
        String remittance = ledger.matches("^(status|info|list|show)$") ? ledger : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + remittance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
