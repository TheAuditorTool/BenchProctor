// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactRecord {


    @GetMapping("/CompactRecord")
    public void compactRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(citation, "http");
        String backorder = tuple.getKey();
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(backorder));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String voucher = mdPolicy.sanitize(mdRendered);
        response.getWriter().print("<div>" + voucher + "</div>");
    }
}
