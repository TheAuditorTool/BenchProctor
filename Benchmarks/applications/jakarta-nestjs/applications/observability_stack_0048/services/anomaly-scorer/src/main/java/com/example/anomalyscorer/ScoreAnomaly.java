// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ScoreAnomaly {


    @POST
    @Path("/ScoreAnomaly")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response scoreAnomaly(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = rawBody != null ? rawBody : "";
        String gauge = String.join(" ", excerpt.split("[ \\t]+"));
        String rawUrl = gauge;
        boolean gateBlocked = true;
        try {
            java.net.URI parsedUri = java.net.URI.create(rawUrl);
            String gateHost = parsedUri.getHost() == null ? "" : parsedUri.getHost();
            java.net.InetAddress gateAddr = java.net.InetAddress.getByName(gateHost);
            gateBlocked = gateAddr.isAnyLocalAddress() || gateAddr.isLoopbackAddress()
                    || gateAddr.isSiteLocalAddress() || gateAddr.isLinkLocalAddress();
        } catch (IllegalArgumentException | java.net.UnknownHostException ignored) {
            gateBlocked = true;
        }
        if (gateBlocked) {
            return Response.status(403).entity("private address blocked").build();
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://alert-router:3000/alert-router/routeAlert").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"telemetry_payload\": \"" + gauge + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
