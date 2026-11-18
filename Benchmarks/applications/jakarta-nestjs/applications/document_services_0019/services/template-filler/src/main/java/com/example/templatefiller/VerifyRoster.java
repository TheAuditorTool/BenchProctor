// SPDX-License-Identifier: Apache-2.0
package com.example.templatefiller;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@Path("/")
class VerifyRoster {


    @GET
    @Path("/VerifyRoster")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyRoster(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        String dossier;
        if (passage.length() > 256) { dossier = passage.substring(0, 256); }
        else { dossier = passage; }
        String socketRaw = String.valueOf(dossier);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
