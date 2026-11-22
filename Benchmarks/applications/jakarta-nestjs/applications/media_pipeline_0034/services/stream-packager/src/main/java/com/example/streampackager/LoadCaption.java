// SPDX-License-Identifier: Apache-2.0
package com.example.streampackager;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
public class LoadCaption {


    @GET
    @Path("/LoadCaption")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadCaption(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = host != null ? host : "";
        String prefix = synopsis.length() > 0 ? synopsis.substring(0, 1).toLowerCase() : "";
        String rendition;
        switch (prefix) {
            case "h": rendition = synopsis.toLowerCase(); break;
            case "f": rendition = synopsis.toUpperCase(); break;
            default: rendition = synopsis.strip(); break;
        }
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(rendition)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
