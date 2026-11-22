// SPDX-License-Identifier: Apache-2.0
package com.example.rulesservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BuildCase {


    @GET
    @Path("/BuildCase")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildCase(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = xForwardedFor != null ? xForwardedFor : "";
        String prefix = excerpt.length() > 0 ? excerpt.substring(0, 1).toLowerCase() : "";
        String verdict;
        switch (prefix) {
            case "h": verdict = excerpt.toLowerCase(); break;
            case "f": verdict = excerpt.toUpperCase(); break;
            default: verdict = excerpt.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(verdict).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String grievance = resolved.toString();
        Files.delete(Paths.get(grievance));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
