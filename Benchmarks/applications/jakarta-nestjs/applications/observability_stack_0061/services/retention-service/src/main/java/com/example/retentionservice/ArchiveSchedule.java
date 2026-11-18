// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class ArchiveSchedule {


    @GET
    @Path("/ArchiveSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveSchedule(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = userAgent != null ? userAgent : "";
        String cohort;
        try { cohort = String.valueOf(Integer.parseInt(headline)); }
        catch (NumberFormatException e) { cohort = headline; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(cohort.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
