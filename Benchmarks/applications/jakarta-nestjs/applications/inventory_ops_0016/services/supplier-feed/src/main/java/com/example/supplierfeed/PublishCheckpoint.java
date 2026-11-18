// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class PublishCheckpoint {


    @GET
    @Path("/PublishCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = origin != null ? origin : "";
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String backorder;
        switch (prefix) {
            case "h": backorder = citation.toLowerCase(); break;
            case "f": backorder = citation.toUpperCase(); break;
            default: backorder = citation.strip(); break;
        }
        java.net.URI parsed = java.net.URI.create(backorder);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { return Response.status(403).build(); }
        String restock = backorder;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(restock)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
