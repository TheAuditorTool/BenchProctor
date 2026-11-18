// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class AuditSummary {


    @POST
    @Path("/AuditSummary")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditSummary(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = field != null ? field : "";
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String bulletin;
        switch (prefix) {
            case "h": bulletin = footnote.toLowerCase(); break;
            case "f": bulletin = footnote.toUpperCase(); break;
            default: bulletin = footnote.strip(); break;
        }
        String heading = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + heading), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
