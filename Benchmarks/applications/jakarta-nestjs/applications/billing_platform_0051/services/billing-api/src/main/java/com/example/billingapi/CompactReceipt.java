// SPDX-License-Identifier: Apache-2.0
package com.example.billingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CompactReceipt {


    @GET
    @Path("/CompactReceipt/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactReceipt(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = pathId;
        String arrears = java.net.URLDecoder.decode(synopsis, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String dunning = policy.sanitize(arrears);
        return Response.ok("<div>" + dunning + "</div>", MediaType.TEXT_HTML).build();
    }
}
