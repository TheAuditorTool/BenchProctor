// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PullSupplierFeed {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/PullSupplierFeed")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pullSupplierFeed(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = xForwardedFor != null ? xForwardedFor : "";
        String restock = normalize(summary);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://allocation-service:3000/allocation-service/solveAllocation").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"inventory_payload\": \"" + restock + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
