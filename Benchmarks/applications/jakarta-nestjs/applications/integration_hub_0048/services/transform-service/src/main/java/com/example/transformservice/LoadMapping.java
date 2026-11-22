// SPDX-License-Identifier: Apache-2.0
package com.example.transformservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class LoadMapping {


    @GET
    @Path("/LoadMapping")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadMapping(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = xForwardedFor != null ? xForwardedFor : "";
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String handshake;
        switch (prefix) {
            case "h": handshake = citation.toLowerCase(); break;
            case "f": handshake = citation.toUpperCase(); break;
            default: handshake = citation.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(handshake).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String heading = resolved.toString();
        Files.delete(Paths.get(heading));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
