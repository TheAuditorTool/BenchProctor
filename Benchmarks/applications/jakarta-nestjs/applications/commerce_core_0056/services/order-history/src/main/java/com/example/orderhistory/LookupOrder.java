// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class LookupOrder {


    @POST
    @Path("/LookupOrder")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response lookupOrder(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = xmlBody;
        request.setAttribute("payload", citation);
        String backorder = String.valueOf(request.getAttribute("payload"));
        String rawUrl = backorder;
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
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://returns-service:3000/returns-service/requestReturn").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"orders_payload\": \"" + backorder + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
