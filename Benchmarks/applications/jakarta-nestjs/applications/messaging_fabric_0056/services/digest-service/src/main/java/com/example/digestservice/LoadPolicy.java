// SPDX-License-Identifier: Apache-2.0
package com.example.digestservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class LoadPolicy {


    @POST
    @Path("/LoadPolicy")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadPolicy(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", footnote);
        String bulletin = container.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(bulletin)) { return Response.status(403).build(); }
        String snippet = "/var/app/data/" + bulletin;
        Files.write(Paths.get(snippet), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
