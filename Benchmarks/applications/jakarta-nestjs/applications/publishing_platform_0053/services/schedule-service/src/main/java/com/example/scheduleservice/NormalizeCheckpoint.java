// SPDX-License-Identifier: Apache-2.0
package com.example.scheduleservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class NormalizeCheckpoint {


    @GET
    @Path("/NormalizeCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : note.split(",")) { tokens.add(token.trim()); }
        String byline = String.join(",", tokens);
        String streamedHtml = "<div class=\"comment\">" + byline + "</div>";
        jakarta.ws.rs.core.StreamingOutput htmlStream = htmlOut -> htmlOut.write(streamedHtml.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        return Response.ok(htmlStream, MediaType.TEXT_HTML).build();
    }
}
