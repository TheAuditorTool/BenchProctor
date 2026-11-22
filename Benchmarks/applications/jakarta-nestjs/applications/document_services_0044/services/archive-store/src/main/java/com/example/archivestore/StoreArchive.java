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


    @POST
    @Path("/StoreArchive")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeArchive(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = rawBody != null ? rawBody : "";
        java.util.Properties property = new java.util.Properties();
        property.setProperty("value", phrase);
        String dossier = property.getProperty("value", "");
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://redaction-service:3000/redaction-service/applyRedaction").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"documents_payload\": \"" + dossier + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
