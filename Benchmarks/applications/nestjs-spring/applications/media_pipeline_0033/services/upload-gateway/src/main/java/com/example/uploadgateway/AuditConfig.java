// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditConfig {


    @PostMapping("/AuditConfig")
    public void auditConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : transcript.split(",")) { tokens.add(token.trim()); }
        String rendition = String.join(",", tokens);
        response.getWriter().print("<div>" + rendition + "</div>");
    }
}
