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
public class ValidateCheckpoint {


    @POST
    @Path("/ValidateCheckpoint")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = rawBody != null ? rawBody : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", headline);
        String remittance = holder.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(remittance)) { return Response.status(403).build(); }
        String dunning = "/var/app/data/" + remittance;
        Files.write(Paths.get(dunning), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
