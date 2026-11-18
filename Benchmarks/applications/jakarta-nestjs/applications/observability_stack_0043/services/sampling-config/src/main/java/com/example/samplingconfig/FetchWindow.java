// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class FetchWindow {


    @GET
    @Path("/FetchWindow")
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchWindow(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = userAgent != null ? userAgent : "";
        String gauge;
        try { gauge = String.valueOf(Integer.parseInt(note)); }
        catch (NumberFormatException e) { gauge = note; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(gauge.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
