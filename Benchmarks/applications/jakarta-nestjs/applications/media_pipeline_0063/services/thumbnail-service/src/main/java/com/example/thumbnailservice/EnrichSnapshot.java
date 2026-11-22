// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class EnrichSnapshot {


    @POST
    @Path("/EnrichSnapshot")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichSnapshot(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = field != null ? field : "";
        String montage = java.net.URLDecoder.decode(snippet, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String rendition = policy.sanitize(montage);
        return Response.ok("<div>" + rendition + "</div>", MediaType.TEXT_HTML).build();
    }
}
