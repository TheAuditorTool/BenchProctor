// SPDX-License-Identifier: Apache-2.0
package com.example.releaseapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ArchiveReport {


    @GET
    @Path("/ArchiveReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveReport(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = userAgent != null ? userAgent : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", footnote);
        String wording = sw.toString();
        return Response.ok("<div>" + wording + "</div>", MediaType.TEXT_HTML).build();
    }
}
