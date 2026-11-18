// SPDX-License-Identifier: Apache-2.0
package com.example.signatureverifier;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class VerifySignature {


    @POST
    @Path("/VerifySignature")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifySignature(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = field != null ? field : "";
        String prefix = synopsis.length() > 0 ? synopsis.substring(0, 1).toLowerCase() : "";
        String handshake;
        switch (prefix) {
            case "h": handshake = synopsis.toLowerCase(); break;
            case "f": handshake = synopsis.toUpperCase(); break;
            default: handshake = synopsis.strip(); break;
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://retry-service:3000/retry-service/queueRetry").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"integrations_payload\": \"" + handshake + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
