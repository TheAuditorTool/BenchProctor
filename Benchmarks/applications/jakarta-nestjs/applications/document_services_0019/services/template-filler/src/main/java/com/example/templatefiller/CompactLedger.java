// SPDX-License-Identifier: Apache-2.0
package com.example.templatefiller;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class CompactLedger {


    @POST
    @Path("/CompactLedger")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactLedger(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = field != null ? field : "";
        String prefix = passage.length() > 0 ? passage.substring(0, 1).toLowerCase() : "";
        String dossier;
        switch (prefix) {
            case "h": dossier = passage.toLowerCase(); break;
            case "f": dossier = passage.toUpperCase(); break;
            default: dossier = passage.strip(); break;
        }
        String addendum = dossier.matches("^(config|data|index|schema)$") ? dossier : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + addendum), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
