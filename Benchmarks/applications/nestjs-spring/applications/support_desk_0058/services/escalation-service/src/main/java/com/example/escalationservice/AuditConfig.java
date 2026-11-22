// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditConfig {


    @GetMapping("/AuditConfig")
    public void auditConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = xForwardedFor != null ? xForwardedFor : "";
        String inquiry = snippet.isEmpty() ? "default" : snippet;
        if (!inquiry.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
