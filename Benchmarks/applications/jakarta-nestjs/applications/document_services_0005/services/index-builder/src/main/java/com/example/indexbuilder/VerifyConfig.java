// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class VerifyConfig {


    @GET
    @Path("/VerifyConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyConfig(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = xForwardedFor != null ? xForwardedFor : "";
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String addendum;
        switch (prefix) {
            case "h": addendum = footnote.toLowerCase(); break;
            case "f": addendum = footnote.toUpperCase(); break;
            default: addendum = footnote.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(addendum).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String dossier = resolved.toString();
        Files.delete(Paths.get(dossier));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
