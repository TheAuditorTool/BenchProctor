// SPDX-License-Identifier: Apache-2.0
package com.example.mandateregistry;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class CompactConfig {


    @GET
    @Path("/CompactConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactConfig(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = xForwardedFor != null ? xForwardedFor : "";
        String prefix = headline.length() > 0 ? headline.substring(0, 1).toLowerCase() : "";
        String disbursement;
        switch (prefix) {
            case "h": disbursement = headline.toLowerCase(); break;
            case "f": disbursement = headline.toUpperCase(); break;
            default: disbursement = headline.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(disbursement).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String remittance = resolved.toString();
        Files.delete(Paths.get(remittance));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
