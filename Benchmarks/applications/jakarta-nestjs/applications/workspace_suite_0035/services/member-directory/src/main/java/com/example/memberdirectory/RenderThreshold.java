// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RenderThreshold {


    @GET
    @Path("/RenderThreshold")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderThreshold(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = referer != null ? referer : "";
        String wording;
        if (paragraph.length() > 256) { wording = paragraph.substring(0, 256); }
        else { wording = paragraph; }
        String transcript = wording.matches("^(status|info|list|show)$") ? wording : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + transcript});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
