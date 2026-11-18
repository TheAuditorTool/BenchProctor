// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class ArchiveRoster {


    @POST
    @Path("/ArchiveRoster")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveRoster(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = field != null ? field : "";
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String parcel;
        switch (prefix) {
            case "h": parcel = citation.toLowerCase(); break;
            case "f": parcel = citation.toUpperCase(); break;
            default: parcel = citation.strip(); break;
        }
        String consignment = parcel.matches("^(config|data|index|schema)$") ? parcel : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + consignment), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
