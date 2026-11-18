// SPDX-License-Identifier: Apache-2.0
package com.example.secretbroker;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class BuildReceipt {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BuildReceipt")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildReceipt(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = java.util.Optional.ofNullable(System.getenv("PLATFORM_INPUT_0054")).orElse("");
        String persona = normalize(snippet);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + persona}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
