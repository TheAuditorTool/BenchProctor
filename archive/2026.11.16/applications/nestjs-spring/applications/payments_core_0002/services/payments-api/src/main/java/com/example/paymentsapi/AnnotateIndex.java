// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateIndex {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/AnnotateIndex")
    public void annotateIndex(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subtitle = sessionToken != null ? sessionToken : "";
        String ledger = normalize(subtitle);
        String remittance = ledger.matches("^(status|info|list|show)$") ? ledger : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + remittance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
