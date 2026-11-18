// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class BuildSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BuildSnapshot")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildSnapshot(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = xForwardedFor != null ? xForwardedFor : "";
        String rendition = normalize(notice);
        String socketRaw = String.valueOf(rendition);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
