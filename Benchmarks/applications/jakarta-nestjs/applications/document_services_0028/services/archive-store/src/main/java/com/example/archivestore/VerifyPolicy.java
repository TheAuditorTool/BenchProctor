// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class VerifyPolicy {


    @POST
    @Path("/VerifyPolicy")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyPolicy(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = field != null ? field : "";
        String prefix = note.length() > 0 ? note.substring(0, 1).toLowerCase() : "";
        String addendum;
        switch (prefix) {
            case "h": addendum = note.toLowerCase(); break;
            case "f": addendum = note.toUpperCase(); break;
            default: addendum = note.strip(); break;
        }
        String dossier = addendum.matches("^(config|data|index|schema)$") ? addendum : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + dossier), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
