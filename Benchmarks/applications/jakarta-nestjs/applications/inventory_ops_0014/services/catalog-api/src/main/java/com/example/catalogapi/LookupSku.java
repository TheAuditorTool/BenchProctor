// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class LookupSku {


    @POST
    @Path("/LookupSku")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response lookupSku(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(excerpt, "body");
        String restock = edge.getKey();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://supplier-feed:3000/supplier-feed/pullSupplierFeed").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"inventory_payload\": \"" + restock + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
