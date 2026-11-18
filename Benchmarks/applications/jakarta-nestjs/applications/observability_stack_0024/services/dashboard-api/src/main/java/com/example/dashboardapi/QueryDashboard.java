// SPDX-License-Identifier: Apache-2.0
package com.example.dashboardapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class QueryDashboard {


    @GET
    @Path("/QueryDashboard")
    @Produces(MediaType.APPLICATION_JSON)
    public Response queryDashboard(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> summary.strip();
        String cohort = valueSupplier.get();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://retention-service:3000/retention-service/sweepRetention").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"telemetry_payload\": \"" + cohort + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
