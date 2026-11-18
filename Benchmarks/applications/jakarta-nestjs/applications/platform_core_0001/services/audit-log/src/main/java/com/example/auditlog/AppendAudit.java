// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class AppendAudit {


    @GET
    @Path("/AppendAudit")
    @Produces(MediaType.APPLICATION_JSON)
    public Response appendAudit(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String tagline = id != null ? id : "";
        byte[] hexBytes = new byte[tagline.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(tagline.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String persona = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://platform-api:3000/platform-api/provisionTenant").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"platform_payload\": \"" + persona + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
