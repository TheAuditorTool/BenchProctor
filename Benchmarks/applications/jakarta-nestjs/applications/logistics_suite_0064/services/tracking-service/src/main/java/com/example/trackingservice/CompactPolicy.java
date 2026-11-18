// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CompactPolicy {


    @GET
    @Path("/CompactPolicy/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactPolicy(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = pathId;
        String parcel = java.net.URLDecoder.decode(transcript, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String consignment = policy.sanitize(parcel);
        return Response.ok("<div>" + consignment + "</div>", MediaType.TEXT_HTML).build();
    }
}
