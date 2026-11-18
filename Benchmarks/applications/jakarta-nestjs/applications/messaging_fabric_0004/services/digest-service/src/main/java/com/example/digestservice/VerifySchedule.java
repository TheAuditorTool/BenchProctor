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
class VerifySchedule {


    @GET
    @Path("/VerifySchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifySchedule(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = xCustomHeader != null ? xCustomHeader : "";
        String bulletin;
        if (paragraph.length() > 256) { bulletin = paragraph.substring(0, 256); }
        else { bulletin = paragraph; }
        Files.write(Paths.get("/var/uploads/" + bulletin), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
