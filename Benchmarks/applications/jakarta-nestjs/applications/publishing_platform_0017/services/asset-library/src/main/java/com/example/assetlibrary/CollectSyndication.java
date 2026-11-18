// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class CollectSyndication {


    @GET
    @Path("/CollectSyndication")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectSyndication(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = xCustomHeader != null ? xCustomHeader : "";
        String addendum;
        if (summary.length() > 256) { addendum = summary.substring(0, 256); }
        else { addendum = summary; }
        Files.write(Paths.get("/var/uploads/" + addendum), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
