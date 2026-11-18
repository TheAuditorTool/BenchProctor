// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class BuildLedger {


    @GET
    @Path("/BuildLedger")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildLedger(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = xCustomHeader != null ? xCustomHeader : "";
        String montage = String.join(" ", passage.split("[ \\t]+"));
        Files.delete(Paths.get("/var/app/data/" + montage));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
