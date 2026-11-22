// SPDX-License-Identifier: Apache-2.0
package com.example.orderapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class FormatReport {


    @GET
    @Path("/FormatReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response formatReport(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = referer != null ? referer : "";
        String backorder;
        if (headline.length() > 256) { backorder = headline.substring(0, 256); }
        else { backorder = headline; }
        String voucher = backorder.matches("^(status|info|list|show)$") ? backorder : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + voucher});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
