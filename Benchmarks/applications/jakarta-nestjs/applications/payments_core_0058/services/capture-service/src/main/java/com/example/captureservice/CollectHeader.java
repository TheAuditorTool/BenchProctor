// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class CollectHeader {


    @GET
    @Path("/CollectHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectHeader(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        String ledger;
        if (caption.length() > 256) { ledger = caption.substring(0, 256); }
        else { ledger = caption; }
        String socketRaw = String.valueOf(ledger);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
