// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ValidateRoster")
    public void validateRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(summary);
        String notice = bulletin.matches("^(status|info|list|show)$") ? bulletin : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + notice}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
