// SPDX-License-Identifier: Apache-2.0
package com.example.watermarkservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@Path("/")
class PublishReport {


    @GET
    @Path("/PublishReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishReport(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String tagline = origin != null ? origin : "";
        String rendition;
        try { rendition = String.valueOf(Integer.parseInt(tagline)); }
        catch (NumberFormatException e) { rendition = tagline; }
        java.net.URI parsedUri = java.net.URI.create(rendition.contains("://") ? rendition : "https://" + rendition);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { return Response.status(403).build(); }
        String montage = rendition;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(montage)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
