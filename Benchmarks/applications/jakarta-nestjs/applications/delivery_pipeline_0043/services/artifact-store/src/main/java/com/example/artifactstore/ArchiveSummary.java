// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class ArchiveSummary {


    @GET
    @Path("/ArchiveSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveSummary(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = xForwardedFor != null ? xForwardedFor : "";
        String prefix = remark.length() > 0 ? remark.substring(0, 1).toLowerCase() : "";
        String note;
        switch (prefix) {
            case "h": note = remark.toLowerCase(); break;
            case "f": note = remark.toUpperCase(); break;
            default: note = remark.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(note).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String phrase = resolved.toString();
        Files.delete(Paths.get(phrase));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
