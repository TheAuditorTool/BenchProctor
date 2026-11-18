// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class AuditConfig {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/AuditConfig")
    public void auditConfig(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = sessionToken != null ? sessionToken : "";
        String gauge = normalize(summary);
        String cohort = gauge.matches("^(config|data|index|schema)$") ? gauge : "config";
        Files.delete(Paths.get("/var/app/data/" + cohort));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
