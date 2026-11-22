// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class CollectSchedule {


    @POST
    @Path("/CollectSchedule")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectSchedule(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subtitle = field != null ? field : "";
        String persona = java.net.URLDecoder.decode(subtitle, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String handshake = policy.sanitize(persona);
        return Response.ok("<div>" + handshake + "</div>", MediaType.TEXT_HTML).build();
    }
}
