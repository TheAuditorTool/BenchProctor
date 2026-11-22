// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditBatch {


    @GetMapping("/AuditBatch")
    public void auditBatch(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = referer != null ? referer : "";
        String addendum = heading.isEmpty() ? "default" : heading;
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + addendum + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
