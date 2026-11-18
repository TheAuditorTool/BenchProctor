// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class SummarizeProfile {


    @GET
    @Path("/SummarizeProfile/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeProfile(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = pathId;
        String ledger = java.net.URLDecoder.decode(caption, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String remittance = policy.sanitize(ledger);
        return Response.ok("<div>" + remittance + "</div>", MediaType.TEXT_HTML).build();
    }
}
