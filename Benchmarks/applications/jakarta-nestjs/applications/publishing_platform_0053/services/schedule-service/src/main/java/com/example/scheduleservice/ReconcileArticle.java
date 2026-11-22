// SPDX-License-Identifier: Apache-2.0
package com.example.scheduleservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ReconcileArticle {


    @GET
    @Path("/ReconcileArticle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileArticle(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(note, "cookie");
        String byline = kv.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", byline}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
