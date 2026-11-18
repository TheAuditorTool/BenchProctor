// SPDX-License-Identifier: Apache-2.0
package com.example.billingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class NormalizeSchedule {


    @GET
    @Path("/NormalizeSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeSchedule(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = id != null ? id : "";
        java.util.function.Supplier<String> valueSupplier = () -> synopsis.strip();
        String arrears = valueSupplier.get();
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(arrears.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
