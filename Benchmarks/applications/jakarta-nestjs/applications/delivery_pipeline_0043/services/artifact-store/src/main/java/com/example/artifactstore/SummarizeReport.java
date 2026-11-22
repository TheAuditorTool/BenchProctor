// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class SummarizeReport {


    @POST
    @Path("/SummarizeReport")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeReport(@jakarta.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = field != null ? field : "";
        String note = java.net.URLDecoder.decode(remark, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String phrase = policy.sanitize(note);
        return Response.ok("<div>" + phrase + "</div>", MediaType.TEXT_HTML).build();
    }
}
