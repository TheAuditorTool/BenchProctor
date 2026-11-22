// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class SummarizeConfig {


    @POST
    @Path("/SummarizeConfig")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeConfig(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String heading = field != null ? field : "";
        String addendum = java.net.URLDecoder.decode(heading, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String byline = policy.sanitize(addendum);
        return Response.ok("<div>" + byline + "</div>", MediaType.TEXT_HTML).build();
    }
}
