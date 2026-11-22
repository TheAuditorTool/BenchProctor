// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class AuditProfile {


    @GET
    @Path("/AuditProfile")
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditProfile(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = xForwardedFor != null ? xForwardedFor : "";
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String remittance;
        switch (prefix) {
            case "h": remittance = footnote.toLowerCase(); break;
            case "f": remittance = footnote.toUpperCase(); break;
            default: remittance = footnote.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(remittance).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String arrears = resolved.toString();
        Files.delete(Paths.get(arrears));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
