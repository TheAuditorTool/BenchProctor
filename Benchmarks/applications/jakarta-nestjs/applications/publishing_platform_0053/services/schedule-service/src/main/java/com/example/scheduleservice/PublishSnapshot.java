// SPDX-License-Identifier: Apache-2.0
package com.example.scheduleservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class PublishSnapshot {


    @GET
    @Path("/PublishSnapshot")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishSnapshot(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = referer != null ? referer : "";
        String byline;
        if (note.length() > 256) { byline = note.substring(0, 256); }
        else { byline = note; }
        String addendum = byline.matches("^(status|info|list|show)$") ? byline : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + addendum});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
