// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactRecord {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/CompactRecord")
    public void compactRecord(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = sessionToken != null ? sessionToken : "";
        String remittance = normalize(passage);
        String disbursement = remittance.matches("^(status|info|list|show)$") ? remittance : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + disbursement}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
