// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class BuildConfig {


    @GET
    @Path("/BuildConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildConfig(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String tagline = userAgent != null ? userAgent : "";
        String persona;
        try { persona = String.valueOf(Integer.parseInt(tagline)); }
        catch (NumberFormatException e) { persona = tagline; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(persona.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
