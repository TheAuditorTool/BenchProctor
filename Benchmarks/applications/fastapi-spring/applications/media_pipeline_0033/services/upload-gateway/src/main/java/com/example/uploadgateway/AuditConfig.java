// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditConfig {


    @GetMapping("/AuditConfig/{pathId}")
    public void auditConfig(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = pathId;
        String rendition;
        if (transcript.length() > 256) { rendition = transcript.substring(0, 256); }
        else { rendition = transcript; }
        response.getWriter().print("<div>" + rendition + "</div>");
    }
}
