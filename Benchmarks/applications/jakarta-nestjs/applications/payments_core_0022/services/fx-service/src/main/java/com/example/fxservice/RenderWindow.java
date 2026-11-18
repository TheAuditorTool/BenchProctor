// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class RenderWindow {


    @POST
    @Path("/RenderWindow")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderWindow(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = field != null ? field : "";
        String prefix = subject.length() > 0 ? subject.substring(0, 1).toLowerCase() : "";
        String ledger;
        switch (prefix) {
            case "h": ledger = subject.toLowerCase(); break;
            case "f": ledger = subject.toUpperCase(); break;
            default: ledger = subject.strip(); break;
        }
        String disbursement = ledger.matches("^(config|data|index|schema)$") ? ledger : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + disbursement), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
