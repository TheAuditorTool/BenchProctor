// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class ExportConfig {


    @GET
    @Path("/ExportConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportConfig(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = id != null ? id : "";
        java.util.function.Supplier<String> valueSupplier = () -> transcript.strip();
        String heading = valueSupplier.get();
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(heading.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
