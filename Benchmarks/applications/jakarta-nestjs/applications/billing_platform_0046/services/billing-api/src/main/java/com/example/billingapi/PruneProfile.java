// SPDX-License-Identifier: Apache-2.0
package com.example.billingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class PruneProfile {


    @POST
    @Path("/PruneProfile")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneProfile(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = field != null ? field : "";
        String prefix = remark.length() > 0 ? remark.substring(0, 1).toLowerCase() : "";
        String remittance;
        switch (prefix) {
            case "h": remittance = remark.toLowerCase(); break;
            case "f": remittance = remark.toUpperCase(); break;
            default: remittance = remark.strip(); break;
        }
        String arrears = remittance.matches("^(config|data|index|schema)$") ? remittance : "config";
        String content = Files.readString(Paths.get("/var/app/data/" + arrears), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
