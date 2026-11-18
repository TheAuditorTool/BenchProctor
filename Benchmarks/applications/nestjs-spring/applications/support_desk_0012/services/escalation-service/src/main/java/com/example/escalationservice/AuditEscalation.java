// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditEscalation {


    @GetMapping("/AuditEscalation/{pathId}")
    public void auditEscalation(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = pathId;
        String grievance = java.net.URLDecoder.decode(summary, java.nio.charset.StandardCharsets.UTF_8);
        String inquiry = grievance.matches("^(plain|markdown|html|text)$") ? grievance : "plain";
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
