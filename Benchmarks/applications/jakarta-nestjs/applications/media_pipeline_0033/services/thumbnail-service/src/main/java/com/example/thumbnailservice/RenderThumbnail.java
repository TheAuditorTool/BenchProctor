// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RenderThumbnail {


    @GET
    @Path("/RenderThumbnail")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderThumbnail(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = origin != null ? origin : "";
        String prefix = transcript.length() > 0 ? transcript.substring(0, 1).toLowerCase() : "";
        String rendition;
        switch (prefix) {
            case "h": rendition = transcript.toLowerCase(); break;
            case "f": rendition = transcript.toUpperCase(); break;
            default: rendition = transcript.strip(); break;
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://upload-gateway:3000/upload-gateway/uploadAsset").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"media_payload\": \"" + rendition + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
