// SPDX-License-Identifier: Apache-2.0
package com.example.mandateregistry;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RegisterMandate {


    @GET
    @Path("/RegisterMandate")
    @Produces(MediaType.APPLICATION_JSON)
    public Response registerMandate(@javax.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = userAgent != null ? userAgent : "";
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://payments-api:3000/payments-api/authorizePayment").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"payments_payload\": \"" + headline + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
