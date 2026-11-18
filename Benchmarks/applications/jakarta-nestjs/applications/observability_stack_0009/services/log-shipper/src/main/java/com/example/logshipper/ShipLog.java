// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ShipLog {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/ShipLog")
    @Produces(MediaType.APPLICATION_JSON)
    public Response shipLog(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0009")).orElse("");
        String gauge = normalize(summary);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://anomaly-scorer:3000/anomaly-scorer/scoreAnomaly").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"telemetry_payload\": \"" + gauge + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
