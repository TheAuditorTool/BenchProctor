// SPDX-License-Identifier: Apache-2.0
package com.example.articleapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditCheckpoint {


    @PostMapping("/AuditCheckpoint")
    public void auditCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : summary.split(",")) { tokens.add(token.trim()); }
        String addendum = String.join(",", tokens);
        response.getWriter().print("<div>" + addendum + "</div>");
    }
}
