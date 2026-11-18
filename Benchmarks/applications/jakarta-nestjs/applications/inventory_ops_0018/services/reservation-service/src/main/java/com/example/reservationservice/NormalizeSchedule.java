// SPDX-License-Identifier: Apache-2.0
package com.example.reservationservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class NormalizeSchedule {


    @POST
    @Path("/NormalizeSchedule")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeSchedule(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = field != null ? field : "";
        String prefix = transcript.length() > 0 ? transcript.substring(0, 1).toLowerCase() : "";
        String backorder;
        switch (prefix) {
            case "h": backorder = transcript.toLowerCase(); break;
            case "f": backorder = transcript.toUpperCase(); break;
            default: backorder = transcript.strip(); break;
        }
        String restock = backorder.matches("^(config|data|index|schema)$") ? backorder : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + restock), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
