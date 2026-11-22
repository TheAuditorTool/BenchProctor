// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
public class RenderPolicy {


    @GET
    @Path("/RenderPolicy")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderPolicy(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(memo);
        String verdict = root.path("value").asText();
        byte[] serBytes = java.util.Base64.getDecoder().decode(verdict);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
