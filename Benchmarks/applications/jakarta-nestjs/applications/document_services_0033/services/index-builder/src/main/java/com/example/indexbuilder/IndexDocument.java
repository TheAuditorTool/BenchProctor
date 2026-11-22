// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class IndexDocument {


    @POST
    @Path("/IndexDocument")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response indexDocument(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = xmlBody;
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> snippet.replace("\t", " ").strip())
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip());
        String addendum = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
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
