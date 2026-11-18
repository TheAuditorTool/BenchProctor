// SPDX-License-Identifier: Apache-2.0
package com.example.configservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RolloutConfig {


    @GET
    @Path("/RolloutConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rolloutConfig(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = id != null ? id : "";
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://platform-api:3000/platform-api/provisionTenant").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"platform_payload\": \"" + excerpt + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
