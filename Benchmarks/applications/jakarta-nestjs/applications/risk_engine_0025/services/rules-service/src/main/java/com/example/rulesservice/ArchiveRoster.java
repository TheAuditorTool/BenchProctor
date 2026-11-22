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
public class ArchiveRoster {


    @GET
    @Path("/ArchiveRoster")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = sessionToken != null ? sessionToken : "";
        String verdict;
        if (excerpt.length() > 256) { verdict = excerpt.substring(0, 256); }
        else { verdict = excerpt; }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(verdict).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String grievance = resolved.toString();
        String content = Files.readString(Paths.get(grievance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
