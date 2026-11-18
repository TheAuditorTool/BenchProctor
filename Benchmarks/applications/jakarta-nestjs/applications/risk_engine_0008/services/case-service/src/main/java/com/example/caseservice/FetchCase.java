// SPDX-License-Identifier: Apache-2.0
package com.example.caseservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class FetchCase {


    @GET
    @Path("/FetchCase")
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchCase(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String verdict = transform.apply(synopsis);
        String socketRaw = String.valueOf(verdict);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
