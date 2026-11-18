// SPDX-License-Identifier: Apache-2.0
package com.example.bridgeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileManifest {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ReconcileManifest")
    public void reconcileManifest(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = sessionToken != null ? sessionToken : "";
        String handshake = normalize(preface);
        String paragraph = handshake.matches("^(status|info|list|show)$") ? handshake : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + paragraph}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
