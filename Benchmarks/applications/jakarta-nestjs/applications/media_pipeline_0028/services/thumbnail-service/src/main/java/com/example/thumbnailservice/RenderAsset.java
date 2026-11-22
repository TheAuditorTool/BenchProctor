// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class RenderAsset {


    @POST
    @Path("/RenderAsset")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderAsset(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = rawBody != null ? rawBody : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", citation);
        String rendition = box.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(rendition)) { return Response.status(403).build(); }
        String montage = "/var/app/data/" + rendition;
        Files.write(Paths.get(montage), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
