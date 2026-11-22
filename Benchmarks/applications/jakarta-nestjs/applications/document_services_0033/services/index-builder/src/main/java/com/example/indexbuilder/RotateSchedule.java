// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class RotateSchedule {


    @POST
    @Path("/RotateSchedule")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateSchedule(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = rawBody != null ? rawBody : "";
        String addendum;
        if (snippet.length() > 256) { addendum = snippet.substring(0, 256); }
        else { addendum = snippet; }
        Files.write(Paths.get("/var/uploads/" + addendum), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
