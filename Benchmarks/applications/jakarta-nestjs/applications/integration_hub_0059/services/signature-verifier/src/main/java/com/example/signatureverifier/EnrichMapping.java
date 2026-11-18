// SPDX-License-Identifier: Apache-2.0
package com.example.signatureverifier;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class EnrichMapping {


    @GET
    @Path("/EnrichMapping")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichMapping(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = userAgent != null ? userAgent : "";
        String handshake;
        try { handshake = String.valueOf(Integer.parseInt(synopsis)); }
        catch (NumberFormatException e) { handshake = synopsis; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(handshake.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
