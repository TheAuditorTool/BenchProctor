// SPDX-License-Identifier: Apache-2.0
package com.example.jobservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class CollectQuota {


    @POST
    @Path("/CollectQuota")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectQuota(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = field != null ? field : "";
        String persona = java.net.URLDecoder.decode(remark, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String handshake = policy.sanitize(persona);
        return Response.ok("<div>" + handshake + "</div>", MediaType.TEXT_HTML).build();
    }
}
