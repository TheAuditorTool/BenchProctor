// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class BuildDecision {


    @GetMapping("/BuildDecision")
    public void buildDecision(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(summary, "body");
        String grievance = pair.getKey();
        com.vladsch.flexmark.parser.Parser mdParser = com.vladsch.flexmark.parser.Parser.builder().build();
        com.vladsch.flexmark.html.HtmlRenderer mdRenderer = com.vladsch.flexmark.html.HtmlRenderer.builder().build();
        String mdRendered = mdRenderer.render(mdParser.parse(grievance));
        org.owasp.html.PolicyFactory mdPolicy = org.owasp.html.Sanitizers.FORMATTING.and(org.owasp.html.Sanitizers.LINKS);
        String verdict = mdPolicy.sanitize(mdRendered);
        response.getWriter().print("<div>" + verdict + "</div>");
    }
}
