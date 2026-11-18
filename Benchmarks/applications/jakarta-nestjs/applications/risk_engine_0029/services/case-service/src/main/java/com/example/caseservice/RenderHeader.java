// SPDX-License-Identifier: Apache-2.0
package com.example.caseservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RenderHeader {


    @GET
    @Path("/RenderHeader/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderHeader(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = pathId;
        String grievance = java.net.URLDecoder.decode(subject, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String verdict = policy.sanitize(grievance);
        return Response.ok("<div>" + verdict + "</div>", MediaType.TEXT_HTML).build();
    }
}
