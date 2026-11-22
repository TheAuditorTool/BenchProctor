// SPDX-License-Identifier: Apache-2.0
package com.example.tracecollector;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class PruneProfile {


    @GET
    @Path("/PruneProfile")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneProfile(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = xForwardedFor != null ? xForwardedFor : "";
        String prefix = paragraph.length() > 0 ? paragraph.substring(0, 1).toLowerCase() : "";
        String gauge;
        switch (prefix) {
            case "h": gauge = paragraph.toLowerCase(); break;
            case "f": gauge = paragraph.toUpperCase(); break;
            default: gauge = paragraph.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(gauge).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String cohort = resolved.toString();
        Files.delete(Paths.get(cohort));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
