// SPDX-License-Identifier: Apache-2.0
package com.example.retryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ExportRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ExportRoster")
    public void exportRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = sessionToken != null ? sessionToken : "";
        String handshake = normalize(synopsis);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(handshake).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String memo = resolved.toString();
        Files.write(Paths.get(memo), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
