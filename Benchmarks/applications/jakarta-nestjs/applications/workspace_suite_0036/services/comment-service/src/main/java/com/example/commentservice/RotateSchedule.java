// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class RotateSchedule {


    @GET
    @Path("/RotateSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateSchedule(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = xCustomHeader != null ? xCustomHeader : "";
        String synopsis;
        if (remark.length() > 256) { synopsis = remark.substring(0, 256); }
        else { synopsis = remark; }
        Files.write(Paths.get("/var/uploads/" + synopsis), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
