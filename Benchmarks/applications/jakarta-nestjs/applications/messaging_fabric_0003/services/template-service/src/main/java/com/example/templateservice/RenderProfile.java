// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RenderProfile {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/RenderProfile")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderProfile(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = java.util.Optional.ofNullable(System.getenv("MESSAGING_INPUT_0003")).orElse("");
        String bulletin = normalize(subject);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + bulletin}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
