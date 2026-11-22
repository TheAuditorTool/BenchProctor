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
public class RotateReceipt {


    @POST
    @Path("/RotateReceipt")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateReceipt(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = rawBody != null ? rawBody : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", citation);
        String dossier = holder.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(dossier)) { return Response.status(403).build(); }
        String addendum = "/var/app/data/" + dossier;
        Files.write(Paths.get(addendum), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
