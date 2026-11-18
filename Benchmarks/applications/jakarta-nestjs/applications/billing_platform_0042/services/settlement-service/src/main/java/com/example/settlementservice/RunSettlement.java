// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RunSettlement {


    @POST
    @Path("/RunSettlement")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response runSettlement(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = rawBody != null ? rawBody : "";
        byte[] raw = remark.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String remittance = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://payment-gateway:3000/payment-gateway/capturePayment").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"billing_payload\": \"" + remittance + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
