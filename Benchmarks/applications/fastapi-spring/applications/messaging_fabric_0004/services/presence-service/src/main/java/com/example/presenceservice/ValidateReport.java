// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateReport {


    @GetMapping("/ValidateReport")
    public void validateReport(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(paragraph, "header");
        String bulletin = edge.getKey();
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(bulletin));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String synopsis = mdPolicy.sanitize(mdRendered);
        response.getWriter().print("<div>" + synopsis + "</div>");
    }
}
