// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class MapField {


    @GET
    @Path("/MapField")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mapField(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        String handshake = snippet.isEmpty() ? "default" : snippet;
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://connector-api:3000/connector-api/invokeConnector").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"integrations_payload\": \"" + handshake + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
