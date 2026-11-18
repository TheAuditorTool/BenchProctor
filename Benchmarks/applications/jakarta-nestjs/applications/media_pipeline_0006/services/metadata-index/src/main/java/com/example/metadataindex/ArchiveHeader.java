// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class ArchiveHeader {


    @GET
    @Path("/ArchiveHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveHeader(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = userAgent != null ? userAgent : "";
        String montage;
        try { montage = String.valueOf(Integer.parseInt(passage)); }
        catch (NumberFormatException e) { montage = passage; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(montage.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
