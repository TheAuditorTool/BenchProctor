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
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
class VerifyReceipt {


    @POST
    @Path("/VerifyReceipt")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyReceipt(@jakarta.validation.constraints.Size(max = 4096) @FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = multipartField != null ? multipartField : "";
        String handshake;
        try { handshake = String.valueOf(Integer.parseInt(excerpt)); }
        catch (NumberFormatException e) { handshake = excerpt; }
        java.net.URI parsedUri = java.net.URI.create(handshake.contains("://") ? handshake : "https://" + handshake);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { return Response.status(403).build(); }
        String persona = handshake;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(persona)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
