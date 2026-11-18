// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderThumbnail {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("media_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RenderThumbnail")
    public void renderThumbnail(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = inboundPayload.value != null ? inboundPayload.value : "";
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(subject));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String rendition = mdPolicy.sanitize(mdRendered);
        response.getWriter().print("<div>" + rendition + "</div>");
    }
}
