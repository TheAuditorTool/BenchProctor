// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
class PublishArtifact {


    @POST
    @Path("/PublishArtifact")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishArtifact(@FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = fileDetail.getFileName();
        String remark;
        try { remark = String.valueOf(Integer.parseInt(wording)); }
        catch (NumberFormatException e) { remark = wording; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://rollback-service:3000/rollback-service/triggerRollback").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"delivery_payload\": \"" + remark + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
