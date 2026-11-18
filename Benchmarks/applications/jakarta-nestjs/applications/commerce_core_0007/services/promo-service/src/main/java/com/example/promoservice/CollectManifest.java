// SPDX-License-Identifier: Apache-2.0
package com.example.promoservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class CollectManifest {


    @GET
    @Path("/CollectManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectManifest(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String heading = userAgent != null ? userAgent : "";
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(heading)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
