// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class CutRelease {


    @POST
    @Path("/CutRelease")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response cutRelease(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = rawBody != null ? rawBody : "";
        String phrase;
        if (summary.length() > 256) { phrase = summary.substring(0, 256); }
        else { phrase = summary; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://rollback-service:3000/rollback-service/triggerRollback").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"delivery_payload\": \"" + phrase + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
