// SPDX-License-Identifier: Apache-2.0
package com.example.devicetrust;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class RenderSnapshot {


    @POST
    @Path("/RenderSnapshot")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderSnapshot(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = rawBody != null ? rawBody : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", paragraph);
        String persona = holder.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(persona)) { return Response.status(403).build(); }
        String blurb = "/var/app/data/" + persona;
        Files.write(Paths.get(blurb), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
