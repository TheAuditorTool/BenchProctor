// SPDX-License-Identifier: Apache-2.0
package com.example.promoservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ApplyPromo {


    @POST
    @Path("/ApplyPromo/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response applyPromo(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String heading = java.util.Optional.ofNullable(commentText).orElse("");
        String voucher;
        if (heading.length() > 256) { voucher = heading.substring(0, 256); }
        else { voucher = heading; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://order-history:3000/order-history/lookupOrder").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"orders_payload\": \"" + voucher + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
