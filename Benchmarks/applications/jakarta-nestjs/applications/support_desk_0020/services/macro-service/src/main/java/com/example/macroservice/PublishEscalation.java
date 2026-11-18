// SPDX-License-Identifier: Apache-2.0
package com.example.macroservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PublishEscalation {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/PublishEscalation")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishEscalation(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(System.getenv("SUPPORT_INPUT_0020")).orElse("");
        String inquiry = normalize(phrase);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + inquiry}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
