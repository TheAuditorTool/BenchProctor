// SPDX-License-Identifier: Apache-2.0
package com.example.secretbroker;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class FetchSecret {


    @POST
    @Path("/FetchSecret/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchSecret(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = java.util.Optional.ofNullable(commentText).orElse("");
        String persona = snippet.replace("\u0000", "");
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://registry-service:3000/registry-service/registerService").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"platform_payload\": \"" + persona + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
