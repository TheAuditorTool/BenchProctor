// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class DispatchCarrier {


    @GET
    @Path("/DispatchCarrier")
    @Produces(MediaType.APPLICATION_JSON)
    public Response dispatchCarrier(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = origin != null ? origin : "";
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String parcel;
        switch (prefix) {
            case "h": parcel = citation.toLowerCase(); break;
            case "f": parcel = citation.toUpperCase(); break;
            default: parcel = citation.strip(); break;
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://manifest-builder:3000/manifest-builder/buildManifest").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"shipping_payload\": \"" + parcel + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
