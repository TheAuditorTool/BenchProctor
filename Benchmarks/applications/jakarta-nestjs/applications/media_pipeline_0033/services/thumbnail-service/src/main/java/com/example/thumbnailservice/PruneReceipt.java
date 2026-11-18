// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class PruneReceipt {


    @GET
    @Path("/PruneReceipt")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneReceipt(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = origin != null ? origin : "";
        String prefix = transcript.length() > 0 ? transcript.substring(0, 1).toLowerCase() : "";
        String rendition;
        switch (prefix) {
            case "h": rendition = transcript.toLowerCase(); break;
            case "f": rendition = transcript.toUpperCase(); break;
            default: rendition = transcript.strip(); break;
        }
        java.net.URI parsed = java.net.URI.create(rendition);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { return Response.status(403).build(); }
        String montage = rendition;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(montage)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
