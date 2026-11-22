// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RenderManifest {


    @GET
    @Path("/RenderManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderManifest(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String tagline = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(tagline, "http");
        String gauge = edge.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", gauge}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
