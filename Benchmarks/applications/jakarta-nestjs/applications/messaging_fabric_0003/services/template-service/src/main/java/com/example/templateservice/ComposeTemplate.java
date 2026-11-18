// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ComposeTemplate {


    @GET
    @Path("/ComposeTemplate/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response composeTemplate(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = pathId;
        String bulletin = subject.isEmpty() ? "default" : subject;
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://presence-service:3000/presence-service/updatePresence").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"messaging_payload\": \"" + bulletin + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
