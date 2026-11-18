// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CompactBundle {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/CompactBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactBundle(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(System.getenv("SHIPPING_INPUT_0023")).orElse("");
        String parcel = normalize(caption);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + parcel}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
