// SPDX-License-Identifier: Apache-2.0
package com.example.tracecollector;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class FormatProfile {


    @GET
    @Path("/FormatProfile")
    @Produces(MediaType.APPLICATION_JSON)
    public Response formatProfile(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = referer != null ? referer : "";
        String gauge;
        if (paragraph.length() > 256) { gauge = paragraph.substring(0, 256); }
        else { gauge = paragraph; }
        String cohort = gauge.matches("^(status|info|list|show)$") ? gauge : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + cohort});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
