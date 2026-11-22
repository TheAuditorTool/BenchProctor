// SPDX-License-Identifier: Apache-2.0
package com.example.fulfillmentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class CompactConfig {


    @GET
    @Path("/CompactConfig/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactConfig(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = pathId;
        String voucher;
        if (subject.length() > 256) { voucher = subject.substring(0, 256); }
        else { voucher = subject; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String backorder = policy.sanitize(voucher);
        return Response.ok("<div>" + backorder + "</div>", MediaType.TEXT_HTML).build();
    }
}
