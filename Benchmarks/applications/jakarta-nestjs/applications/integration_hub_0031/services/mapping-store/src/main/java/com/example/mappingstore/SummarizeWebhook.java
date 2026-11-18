// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class SummarizeWebhook {


    @POST
    @Path("/SummarizeWebhook")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeWebhook(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = field != null ? field : "";
        String prefix = snippet.length() > 0 ? snippet.substring(0, 1).toLowerCase() : "";
        String handshake;
        switch (prefix) {
            case "h": handshake = snippet.toLowerCase(); break;
            case "f": handshake = snippet.toUpperCase(); break;
            default: handshake = snippet.strip(); break;
        }
        String paragraph = handshake.matches("^(config|data|index|schema)$") ? handshake : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + paragraph), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
