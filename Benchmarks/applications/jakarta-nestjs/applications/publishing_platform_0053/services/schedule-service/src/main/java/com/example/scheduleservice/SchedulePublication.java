// SPDX-License-Identifier: Apache-2.0
package com.example.scheduleservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class SchedulePublication {


    @GET
    @Path("/SchedulePublication")
    @Produces(MediaType.APPLICATION_JSON)
    public Response schedulePublication(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = referer != null ? referer : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", note);
        String byline = box.getProperty("value", "");
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://asset-library:3000/asset-library/attachAsset").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"publishing_payload\": \"" + byline + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
