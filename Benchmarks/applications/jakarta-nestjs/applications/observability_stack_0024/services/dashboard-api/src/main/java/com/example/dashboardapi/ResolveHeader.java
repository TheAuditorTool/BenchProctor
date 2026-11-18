// SPDX-License-Identifier: Apache-2.0
package com.example.dashboardapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class ResolveHeader {


    @GET
    @Path("/ResolveHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveHeader(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = userAgent != null ? userAgent : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(summary.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String cohort = String.join(",", lowered);
        String socketRaw = String.valueOf(cohort);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
