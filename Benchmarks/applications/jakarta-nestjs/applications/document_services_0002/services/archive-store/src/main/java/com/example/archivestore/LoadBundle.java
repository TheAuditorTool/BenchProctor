// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class LoadBundle {


    @GET
    @Path("/LoadBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadBundle(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(wording, "form");
        String addendum = entry.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", addendum}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
