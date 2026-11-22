// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class RaiseEscalation {


    @GET
    @Path("/RaiseEscalation")
    @Produces(MediaType.APPLICATION_JSON)
    public Response raiseEscalation(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = host != null ? host : "";
        String prefix = preface.length() > 0 ? preface.substring(0, 1).toLowerCase() : "";
        String grievance;
        switch (prefix) {
            case "h": grievance = preface.toLowerCase(); break;
            case "f": grievance = preface.toUpperCase(); break;
            default: grievance = preface.strip(); break;
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://macro-service:3000/macro-service/applyMacro").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"support_payload\": \"" + grievance + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
