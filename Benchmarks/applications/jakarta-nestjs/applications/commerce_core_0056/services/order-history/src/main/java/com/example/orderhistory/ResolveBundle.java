// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class ResolveBundle {


    @GET
    @Path("/ResolveBundle")
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveBundle(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = userAgent != null ? userAgent : "";
        String backorder;
        try { backorder = String.valueOf(Integer.parseInt(citation)); }
        catch (NumberFormatException e) { backorder = citation; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(backorder.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
