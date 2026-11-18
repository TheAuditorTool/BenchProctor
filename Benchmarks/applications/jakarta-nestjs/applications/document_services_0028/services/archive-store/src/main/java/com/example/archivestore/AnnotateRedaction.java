// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class AnnotateRedaction {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/AnnotateRedaction")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateRedaction(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = xForwardedFor != null ? xForwardedFor : "";
        String addendum = normalize(note);
        String socketRaw = String.valueOf(addendum);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
