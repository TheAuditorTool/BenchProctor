// SPDX-License-Identifier: Apache-2.0
package com.example.attachmentstore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class PublishManifest {


    @POST
    @Path("/PublishManifest")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishManifest(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String blurb = field != null ? field : "";
        String inquiry = java.net.URLDecoder.decode(blurb, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String grievance = policy.sanitize(inquiry);
        return Response.ok("<div>" + grievance + "</div>", MediaType.TEXT_HTML).build();
    }
}
