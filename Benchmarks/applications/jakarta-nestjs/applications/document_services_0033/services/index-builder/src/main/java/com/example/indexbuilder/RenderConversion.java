// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class RenderConversion {


    @GET
    @Path("/RenderConversion")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderConversion(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = referer != null ? referer : "";
        String addendum;
        if (snippet.length() > 256) { addendum = snippet.substring(0, 256); }
        else { addendum = snippet; }
        String dossier = addendum.matches("^(status|info|list|show)$") ? addendum : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + dossier});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
