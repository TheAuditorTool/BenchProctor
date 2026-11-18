// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class UpdateCart {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("orders_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/UpdateCart")
    public void updateCart(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = inboundPayload.value != null ? inboundPayload.value : "";
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(transcript));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String backorder = mdPolicy.sanitize(mdRendered);
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
