// SPDX-License-Identifier: Apache-2.0
package com.example.jobservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class AnnotateQuota {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/AnnotateQuota")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateQuota(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = java.util.Optional.ofNullable(System.getenv("PLATFORM_INPUT_0015")).orElse("");
        String handshake = normalize(note);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + handshake}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
