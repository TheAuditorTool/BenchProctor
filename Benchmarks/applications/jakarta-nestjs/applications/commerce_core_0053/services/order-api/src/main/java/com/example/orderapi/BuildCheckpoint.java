// SPDX-License-Identifier: Apache-2.0
package com.example.orderapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class BuildCheckpoint {


    @GET
    @Path("/BuildCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = sessionToken != null ? sessionToken : "";
        String voucher;
        try { voucher = new String(java.util.Base64.getDecoder().decode(memo), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { voucher = memo; }
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(voucher));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String backorder = mdPolicy.sanitize(mdRendered);
        return Response.ok("<div>" + backorder + "</div>", MediaType.TEXT_HTML).build();
    }
}
