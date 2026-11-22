// SPDX-License-Identifier: Apache-2.0
package com.example.orderapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class PlaceOrder {


    @POST
    @Path("/PlaceOrder")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response placeOrder(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = rawBody != null ? rawBody : "";
        String backorder = String.join(" ", headline.split("[ \\t]+"));
        String gateUrl = backorder;
        boolean gateAllowed = false;
        try {
            java.net.URI gateUri = new java.net.URI(gateUrl);
            gateAllowed = ("http".equalsIgnoreCase(gateUri.getScheme()) || "https".equalsIgnoreCase(gateUri.getScheme()))
                    && gateUri.getRawUserInfo() == null
                    && !java.util.regex.Pattern.compile("[\\x00-\\x20\\x7f\\\\]").matcher(gateUrl).find()
                    && gateUri.getHost() != null
                    && java.util.Set.of("api.svc.local", "cdn.acmecdn.net").contains(gateUri.getHost());
        } catch (java.net.URISyntaxException ignored) {
            gateAllowed = false;
        }
        if (!gateAllowed) {
            return Response.status(403).entity("forbidden host").build();
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://cart-service:3000/cart-service/updateCart").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"orders_payload\": \"" + backorder + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
