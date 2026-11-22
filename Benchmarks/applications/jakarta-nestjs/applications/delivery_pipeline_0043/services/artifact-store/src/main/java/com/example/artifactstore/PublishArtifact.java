// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class PublishArtifact {


    @POST
    @Path("/PublishArtifact")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishArtifact(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = rawBody != null ? rawBody : "";
        String note = String.join(" ", remark.split("[ \\t]+"));
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://canary-controller:3000/canary-controller/promoteCanary").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"delivery_payload\": \"" + note + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
