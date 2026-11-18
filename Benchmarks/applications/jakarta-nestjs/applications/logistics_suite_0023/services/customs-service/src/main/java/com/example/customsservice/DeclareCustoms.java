// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class DeclareCustoms {


    @GET
    @Path("/DeclareCustoms")
    @Produces(MediaType.APPLICATION_JSON)
    public Response declareCustoms(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        String parcel;
        if (caption.length() > 256) { parcel = caption.substring(0, 256); }
        else { parcel = caption; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://rate-shopper:3000/rate-shopper/shopRate").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"shipping_payload\": \"" + parcel + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
