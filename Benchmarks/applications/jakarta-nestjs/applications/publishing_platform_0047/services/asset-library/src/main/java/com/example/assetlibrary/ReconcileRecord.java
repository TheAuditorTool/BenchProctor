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
class ReconcileRecord {


    @GET
    @Path("/ReconcileRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileRecord(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = xCustomHeader != null ? xCustomHeader : "";
        String byline;
        if (synopsis.length() > 256) { byline = synopsis.substring(0, 256); }
        else { byline = synopsis; }
        Files.write(Paths.get("/var/uploads/" + byline), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
