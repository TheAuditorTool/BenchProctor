// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class VerifyHeader {


    @GET
    @Path("/VerifyHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyHeader(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = xCustomHeader != null ? xCustomHeader : "";
        String bulletin = String.join(" ", preface.split("[ \\t]+"));
        Files.delete(Paths.get("/var/app/data/" + bulletin));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
