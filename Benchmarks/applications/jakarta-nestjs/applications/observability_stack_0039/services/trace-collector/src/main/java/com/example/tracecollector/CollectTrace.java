// SPDX-License-Identifier: Apache-2.0
package com.example.tracecollector;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectTrace {


    @POST
    @Path("/CollectTrace")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectTrace(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = xmlBody;
        request.setAttribute("wrapper", caption);
        String cohort = String.valueOf(request.getAttribute("wrapper"));
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://anomaly-scorer:3000/anomaly-scorer/scoreAnomaly").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"telemetry_payload\": \"" + cohort + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
