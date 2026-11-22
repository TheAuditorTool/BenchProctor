// SPDX-License-Identifier: Apache-2.0
package com.example.cyclecount;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class AnnotateSchedule {


    @GET
    @Path("/AnnotateSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateSchedule(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(memo, "query");
        String backorder = edge.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", backorder}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
