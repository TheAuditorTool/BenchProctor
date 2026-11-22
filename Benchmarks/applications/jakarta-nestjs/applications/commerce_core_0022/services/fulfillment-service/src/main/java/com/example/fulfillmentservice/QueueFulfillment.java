// SPDX-License-Identifier: Apache-2.0
package com.example.fulfillmentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.annotation.security.RolesAllowed;

@Path("/")
public class QueueFulfillment {


    @GET
    @Path("/QueueFulfillment/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    @RolesAllowed("USER")
    public Response queueFulfillment(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = pathId;
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("[ \\t]+", " ");
        lengthGuard.accept(subject);
        String voucher = normalizer.apply(subject);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://promo-service:3000/promo-service/applyPromo").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"orders_payload\": \"" + voucher + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
