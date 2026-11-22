// SPDX-License-Identifier: Apache-2.0
package com.example.streampackager;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
public class EnrichSchedule {


    @GET
    @Path("/EnrichSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichSchedule(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(synopsis);
        String rendition = root.path("value").asText();
        byte[] serBytes = java.util.Base64.getDecoder().decode(rendition);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
