// SPDX-License-Identifier: Apache-2.0
package com.example.fulfillmentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class VerifyPolicy {


    @GET
    @Path("/VerifyPolicy")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyPolicy(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = referer != null ? referer : "";
        String voucher;
        if (subject.length() > 256) { voucher = subject.substring(0, 256); }
        else { voucher = subject; }
        String backorder = voucher.matches("^(status|info|list|show)$") ? voucher : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + backorder});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
