// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class MergeHeader {


    @GET
    @Path("/MergeHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeHeader(@jakarta.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = sessionToken != null ? sessionToken : "";
        String remark;
        try { remark = new String(java.util.Base64.getDecoder().decode(preface), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { remark = preface; }
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(remark));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String wording = mdPolicy.sanitize(mdRendered);
        return Response.ok("<div>" + wording + "</div>", MediaType.TEXT_HTML).build();
    }
}
