// SPDX-License-Identifier: Apache-2.0
package com.example.caseservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class OpenCase {


    @GET
    @Path("/OpenCase")
    @Produces(MediaType.APPLICATION_JSON)
    public Response openCase(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = xCustomHeader != null ? xCustomHeader : "";
        String grievance;
        if (summary.length() > 256) { grievance = summary.substring(0, 256); }
        else { grievance = summary; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://alert-triage:3000/alert-triage/triageAlert").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"risk_payload\": \"" + grievance + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
