// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ReconcileSchedule {


    @GET
    @Path("/ReconcileSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileSchedule(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(headline, "json");
        String disbursement = edge.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", disbursement}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
