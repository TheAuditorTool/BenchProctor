// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class EnrichReceipt {


    @GET
    @Path("/EnrichReceipt")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichReceipt(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(notice, "cookie");
        String rendition = pair.getKey();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(rendition)) { return Response.status(403).build(); }
        String montage = rendition;
        new ProcessBuilder(montage).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
