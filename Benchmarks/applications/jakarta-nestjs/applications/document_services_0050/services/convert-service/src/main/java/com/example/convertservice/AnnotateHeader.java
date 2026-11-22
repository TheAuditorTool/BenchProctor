// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class AnnotateHeader {


    @GET
    @Path("/AnnotateHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateHeader(@jakarta.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = sessionToken != null ? sessionToken : "";
        String dossier;
        if (citation.length() > 256) { dossier = citation.substring(0, 256); }
        else { dossier = citation; }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(dossier).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String addendum = resolved.toString();
        String content = Files.readString(Paths.get(addendum), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
