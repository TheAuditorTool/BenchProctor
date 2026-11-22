// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class LoadRecord {


    @GET
    @Path("/LoadRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadRecord(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : note.split(",")) { tokens.add(token.trim()); }
        String cohort = String.join(",", tokens);
        String gauge = cohort.matches("^(status|info|list|show)$") ? cohort : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + gauge}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
