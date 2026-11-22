// SPDX-License-Identifier: Apache-2.0
package com.example.slamonitor;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RenderCheckpoint {


    @GET
    @Path("/RenderCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderCheckpoint(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = referer != null ? referer : "";
        String grievance;
        if (phrase.length() > 256) { grievance = phrase.substring(0, 256); }
        else { grievance = phrase; }
        String inquiry = grievance.matches("^(status|info|list|show)$") ? grievance : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + inquiry});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
