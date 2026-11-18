// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.annotation.security.RolesAllowed;

@Path("/")
class UpdatePresence {


    @GET
    @Path("/UpdatePresence")
    @Produces(MediaType.APPLICATION_JSON)
    @RolesAllowed("USER")
    public Response updatePresence(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = authorization != null ? authorization : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String bulletin = transform.apply(preface);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://template-service:3000/template-service/composeTemplate").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"messaging_payload\": \"" + bulletin + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
