// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class ExportManifest {

    record FormData(String payload) {}

    @GET
    @Path("/ExportManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportManifest(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = referer != null ? referer : "";
        FormData payload = new FormData(preface);
        String grievance = payload.payload();
        if (!grievance.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { return Response.status(400).build(); }
        Files.write(Paths.get("/var/uploads/" + grievance), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
