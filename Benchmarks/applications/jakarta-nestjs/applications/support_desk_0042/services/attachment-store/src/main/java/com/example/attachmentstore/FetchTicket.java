// SPDX-License-Identifier: Apache-2.0
package com.example.attachmentstore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class FetchTicket {


    @GET
    @Path("/FetchTicket")
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchTicket(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String blurb = referer != null ? referer : "";
        String inquiry;
        if (blurb.length() > 256) { inquiry = blurb.substring(0, 256); }
        else { inquiry = blurb; }
        String grievance = inquiry.matches("^(status|info|list|show)$") ? inquiry : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + grievance});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
