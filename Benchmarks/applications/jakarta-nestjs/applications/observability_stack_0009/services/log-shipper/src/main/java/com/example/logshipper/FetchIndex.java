// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class FetchIndex {


    @GET
    @Path("/FetchIndex/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchIndex(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = pathId;
        String gauge = java.net.URLDecoder.decode(summary, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String cohort = policy.sanitize(gauge);
        return Response.ok("<div>" + cohort + "</div>", MediaType.TEXT_HTML).build();
    }
}
