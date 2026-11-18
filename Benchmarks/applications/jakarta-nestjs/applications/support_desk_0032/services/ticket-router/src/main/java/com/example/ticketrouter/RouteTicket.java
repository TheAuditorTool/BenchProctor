// SPDX-License-Identifier: Apache-2.0
package com.example.ticketrouter;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RouteTicket {


    @GET
    @Path("/RouteTicket")
    @Produces(MediaType.APPLICATION_JSON)
    public Response routeTicket(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = xCustomHeader != null ? xCustomHeader : "";
        String inquiry = String.join(" ", note.split("[ \\t]+"));
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://knowledge-index:3000/knowledge-index/searchKnowledge").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"support_payload\": \"" + inquiry + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
