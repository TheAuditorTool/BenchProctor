// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/AuditSnapshot", consumes="text/plain")
    public void auditSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = rawBody != null ? rawBody : "";
        String inquiry = normalize(remark);
        if (!inquiry.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
