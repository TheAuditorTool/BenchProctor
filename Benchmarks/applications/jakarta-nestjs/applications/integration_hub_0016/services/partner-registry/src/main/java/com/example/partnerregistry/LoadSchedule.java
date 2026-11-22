// SPDX-License-Identifier: Apache-2.0
package com.example.partnerregistry;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class LoadSchedule {


    @POST
    @Path("/LoadSchedule")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadSchedule(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = field != null ? field : "";
        String handshake = java.net.URLDecoder.decode(wording, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String subject = policy.sanitize(handshake);
        return Response.ok("<div>" + subject + "</div>", MediaType.TEXT_HTML).build();
    }
}
