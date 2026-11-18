// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactBatch {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/CompactBatch")
    public void compactBatch(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = sessionToken != null ? sessionToken : "";
        String inquiry = normalize(phrase);
        String grievance = inquiry.matches("^(status|info|list|show)$") ? inquiry : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + grievance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
