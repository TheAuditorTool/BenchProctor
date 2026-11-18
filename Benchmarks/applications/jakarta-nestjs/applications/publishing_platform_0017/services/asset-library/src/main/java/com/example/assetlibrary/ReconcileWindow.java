// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class ReconcileWindow {


    @GET
    @Path("/ReconcileWindow")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileWindow(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = userAgent != null ? userAgent : "";
        String addendum;
        try { addendum = String.valueOf(Integer.parseInt(summary)); }
        catch (NumberFormatException e) { addendum = summary; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(addendum.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
