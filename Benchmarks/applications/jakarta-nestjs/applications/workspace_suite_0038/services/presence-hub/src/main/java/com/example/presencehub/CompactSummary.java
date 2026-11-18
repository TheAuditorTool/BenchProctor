// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
class CompactSummary {


    @GET
    @Path("/CompactSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactSummary(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = xCustomHeader != null ? xCustomHeader : "";
        String remark;
        if (preface.length() > 256) { remark = preface.substring(0, 256); }
        else { remark = preface; }
        Files.write(Paths.get("/var/uploads/" + remark), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
