// SPDX-License-Identifier: Apache-2.0
package com.example.recoveryservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PublishConfig {


    @GET
    @Path("/PublishConfig/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishConfig(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = pathId;
        String persona = java.net.URLDecoder.decode(paragraph, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String synopsis = policy.sanitize(persona);
        return Response.ok("<div>" + synopsis + "</div>", MediaType.TEXT_HTML).build();
    }
}
