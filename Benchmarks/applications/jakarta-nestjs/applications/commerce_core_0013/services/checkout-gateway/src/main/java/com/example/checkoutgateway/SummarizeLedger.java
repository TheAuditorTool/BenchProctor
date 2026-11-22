// SPDX-License-Identifier: Apache-2.0
package com.example.checkoutgateway;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class SummarizeLedger {


    @POST
    @Path("/SummarizeLedger")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response summarizeLedger(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = field != null ? field : "";
        String backorder = java.net.URLDecoder.decode(wording, java.nio.charset.StandardCharsets.UTF_8);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String voucher = policy.sanitize(backorder);
        return Response.ok("<div>" + voucher + "</div>", MediaType.TEXT_HTML).build();
    }
}
