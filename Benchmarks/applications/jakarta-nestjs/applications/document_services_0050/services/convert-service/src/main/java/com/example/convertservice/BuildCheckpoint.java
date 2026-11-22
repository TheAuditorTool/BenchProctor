// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class BuildCheckpoint {


    @GET
    @Path("/BuildCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = referer != null ? referer : "";
        String dossier;
        if (citation.length() > 256) { dossier = citation.substring(0, 256); }
        else { dossier = citation; }
        String addendum = dossier.matches("^(status|info|list|show)$") ? dossier : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + addendum});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
