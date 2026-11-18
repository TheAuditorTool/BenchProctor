// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
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
        String footnote = origin != null ? origin : "";
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String wording;
        switch (prefix) {
            case "h": wording = footnote.toLowerCase(); break;
            case "f": wording = footnote.toUpperCase(); break;
            default: wording = footnote.strip(); break;
        }
        java.net.URI parsed = java.net.URI.create(wording);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { return Response.status(403).build(); }
        String note = wording;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(note)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
