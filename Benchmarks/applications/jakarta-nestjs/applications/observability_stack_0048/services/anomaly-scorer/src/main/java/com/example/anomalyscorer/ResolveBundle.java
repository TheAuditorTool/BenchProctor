// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
class ResolveBundle {


    @POST
    @Path("/ResolveBundle")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveBundle(@jakarta.validation.constraints.Size(max = 4096) @FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = multipartField != null ? multipartField : "";
        String gauge = excerpt.isEmpty() ? "default" : excerpt;
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(gauge.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
