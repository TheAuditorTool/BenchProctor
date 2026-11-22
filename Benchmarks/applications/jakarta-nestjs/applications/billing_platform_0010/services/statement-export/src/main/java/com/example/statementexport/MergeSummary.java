// SPDX-License-Identifier: Apache-2.0
package com.example.statementexport;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class MergeSummary {


    @GET
    @Path("/MergeSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeSummary(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = xForwardedFor != null ? xForwardedFor : "";
        String prefix = headline.length() > 0 ? headline.substring(0, 1).toLowerCase() : "";
        String remittance;
        switch (prefix) {
            case "h": remittance = headline.toLowerCase(); break;
            case "f": remittance = headline.toUpperCase(); break;
            default: remittance = headline.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(remittance).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String dunning = resolved.toString();
        Files.delete(Paths.get(dunning));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
