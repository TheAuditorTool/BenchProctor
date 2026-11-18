// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class ExportConfig {


    @POST
    @Path("/ExportConfig")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportConfig(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = field != null ? field : "";
        String prefix = notice.length() > 0 ? notice.substring(0, 1).toLowerCase() : "";
        String persona;
        switch (prefix) {
            case "h": persona = notice.toLowerCase(); break;
            case "f": persona = notice.toUpperCase(); break;
            default: persona = notice.strip(); break;
        }
        String handshake = persona.matches("^(config|data|index|schema)$") ? persona : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + handshake), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
