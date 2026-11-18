// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class ReconcileProfile {


    @POST
    @Path("/ReconcileProfile")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileProfile(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = rawBody != null ? rawBody : "";
        byte[] raw = passage.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String montage = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        java.net.URI parsed = java.net.URI.create(montage);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { return Response.status(403).build(); }
        String rendition = montage;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(rendition)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
