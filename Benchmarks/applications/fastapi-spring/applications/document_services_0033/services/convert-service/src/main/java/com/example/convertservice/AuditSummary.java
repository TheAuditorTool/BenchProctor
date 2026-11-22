// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class AuditSummary {

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @GetMapping("/AuditSummary")
    public void auditSummary(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = authorization != null ? authorization : "";
        FormData payload = new FormData(snippet);
        String addendum = payload.getPayload();
        String content = Files.readString(Paths.get("/var/app/data/" + addendum), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
