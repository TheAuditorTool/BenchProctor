// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class BuildCheckpoint {


    @GET
    @Path("/BuildCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildCheckpoint(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = referer != null ? referer : "";
        String addendum;
        if (footnote.length() > 256) { addendum = footnote.substring(0, 256); }
        else { addendum = footnote; }
        String dossier = addendum.matches("^(status|info|list|show)$") ? addendum : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + dossier});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
