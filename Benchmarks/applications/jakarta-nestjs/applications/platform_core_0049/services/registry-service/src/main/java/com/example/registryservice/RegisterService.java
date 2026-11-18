// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RegisterService {


    @GET
    @Path("/RegisterService/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response registerService(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = pathId;
        String persona = java.net.URLDecoder.decode(notice, java.nio.charset.StandardCharsets.UTF_8);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://config-service:3000/config-service/rolloutConfig").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"platform_payload\": \"" + persona + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
