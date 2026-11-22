// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class StoreArchive {


    @GET
    @Path("/StoreArchive")
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeArchive(@javax.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = sessionToken != null ? sessionToken : "";
        String addendum;
        if (preface.length() > 256) { addendum = preface.substring(0, 256); }
        else { addendum = preface; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://convert-service:3000/convert-service/runConversion").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"documents_payload\": \"" + addendum + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
