// SPDX-License-Identifier: Apache-2.0
package com.example.recoveryservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class SummarizeBundle {


    @GET
    @Path("/SummarizeBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeBundle(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = origin != null ? origin : "";
        String prefix = paragraph.length() > 0 ? paragraph.substring(0, 1).toLowerCase() : "";
        String persona;
        switch (prefix) {
            case "h": persona = paragraph.toLowerCase(); break;
            case "f": persona = paragraph.toUpperCase(); break;
            default: persona = paragraph.strip(); break;
        }
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(persona)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
