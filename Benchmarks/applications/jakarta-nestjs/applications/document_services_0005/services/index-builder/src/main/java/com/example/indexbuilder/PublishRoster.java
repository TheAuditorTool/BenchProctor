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
public class PublishRoster {


    @POST
    @Path("/PublishRoster")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishRoster(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", footnote);
        String addendum = holder.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(addendum)) { return Response.status(403).build(); }
        String dossier = "/var/app/data/" + addendum;
        Files.write(Paths.get(dossier), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
