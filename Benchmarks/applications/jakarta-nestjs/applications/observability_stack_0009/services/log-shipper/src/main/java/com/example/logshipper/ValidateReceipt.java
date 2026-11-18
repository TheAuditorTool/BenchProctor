// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class ValidateReceipt {


    @GET
    @Path("/ValidateReceipt")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateReceipt(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String gauge = transform.apply(summary);
        String socketRaw = String.valueOf(gauge);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
