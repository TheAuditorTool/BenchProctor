// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class PublishPolicy {


    @GET
    @Path("/PublishPolicy")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishPolicy(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(transcript, "header");
        String consignment = pair.getKey();
        Runtime.getRuntime().exec(new String[]{"echo", consignment}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
