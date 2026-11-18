// SPDX-License-Identifier: Apache-2.0
package com.example.alertrouter;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditDigest {


    @GetMapping("/AuditDigest/{pathId}")
    public void auditDigest(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = pathId;
        String gauge;
        if (excerpt.length() > 256) { gauge = excerpt.substring(0, 256); }
        else { gauge = excerpt; }
        response.getWriter().print("<div>" + gauge + "</div>");
    }
}
