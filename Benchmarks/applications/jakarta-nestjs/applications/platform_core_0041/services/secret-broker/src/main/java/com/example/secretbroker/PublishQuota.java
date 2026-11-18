// SPDX-License-Identifier: Apache-2.0
package com.example.secretbroker;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class PublishQuota {


    @GET
    @Path("/PublishQuota")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishQuota(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = id != null ? id : "";
        java.util.function.Supplier<String> valueSupplier = () -> passage.strip();
        String persona = valueSupplier.get();
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(persona.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
