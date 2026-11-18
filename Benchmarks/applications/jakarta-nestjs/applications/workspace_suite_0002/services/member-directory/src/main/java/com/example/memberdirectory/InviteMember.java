// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class InviteMember {


    @GET
    @Path("/InviteMember")
    @Produces(MediaType.APPLICATION_JSON)
    public Response inviteMember(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(transcript, "form");
        String heading = entry.getKey();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://comment-service:3000/comment-service/postComment").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"workspace_payload\": \"" + heading + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
