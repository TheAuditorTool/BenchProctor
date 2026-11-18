// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class AnnotateManifest {


    @POST
    @Path("/AnnotateManifest")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateManifest(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = field != null ? field : "";
        String prefix = caption.length() > 0 ? caption.substring(0, 1).toLowerCase() : "";
        String ledger;
        switch (prefix) {
            case "h": ledger = caption.toLowerCase(); break;
            case "f": ledger = caption.toUpperCase(); break;
            default: ledger = caption.strip(); break;
        }
        String remittance = ledger.matches("^(config|data|index|schema)$") ? ledger : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + remittance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
