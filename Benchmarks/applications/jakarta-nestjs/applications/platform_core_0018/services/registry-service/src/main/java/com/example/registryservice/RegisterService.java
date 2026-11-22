// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RegisterService {


    @GET
    @Path("/RegisterService")
    @Produces(MediaType.APPLICATION_JSON)
    public Response registerService(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subtitle = host != null ? host : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(subtitle, "form");
        String persona = kv.getKey();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://audit-log:3000/audit-log/appendAudit").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"platform_payload\": \"" + persona + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
