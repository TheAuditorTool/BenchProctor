// SPDX-License-Identifier: Apache-2.0
package com.example.partnerregistry;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ResolveWindow {


    @GET
    @Path("/ResolveWindow")
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveWindow(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String blurb = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : blurb.split(",")) { tokens.add(token.trim()); }
        String handshake = String.join(",", tokens);
        new ProcessBuilder("echo", handshake).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
