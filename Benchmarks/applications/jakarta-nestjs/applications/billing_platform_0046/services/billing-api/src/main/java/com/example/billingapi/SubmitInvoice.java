// SPDX-License-Identifier: Apache-2.0
package com.example.billingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class SubmitInvoice {


    @GET
    @Path("/SubmitInvoice")
    @Produces(MediaType.APPLICATION_JSON)
    public Response submitInvoice(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(remark);
        String remittance = root.path("value").asText();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://settlement-service:3000/settlement-service/runSettlement").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"billing_payload\": \"" + remittance + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
