// SPDX-License-Identifier: Apache-2.0
package com.example.attachmentstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class StoreAttachment {


    @POST
    @Path("/StoreAttachment/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeAttachment(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        if (request.getUserPrincipal() == null) {
            return Response.status(401).entity("unauthorized").build();
        }
        String remark = java.util.Optional.ofNullable(commentText).orElse("");
        String inquiry = remark.replace("\u0000", "");
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://survey-service:3000/survey-service/sendSurvey").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"support_payload\": \"" + inquiry + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
