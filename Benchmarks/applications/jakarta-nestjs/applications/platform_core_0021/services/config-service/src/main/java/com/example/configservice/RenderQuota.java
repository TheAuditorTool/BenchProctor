// SPDX-License-Identifier: Apache-2.0
package com.example.configservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class RenderQuota {


    @POST
    @Path("/RenderQuota")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderQuota(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = rawBody != null ? rawBody : "";
        String handshake = String.join(" ", excerpt.split("[ \\t]+"));
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(handshake)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
