// SPDX-License-Identifier: Apache-2.0
package com.example.mfaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveBundle {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ResolveBundle")
    public void resolveBundle(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = sessionToken != null ? sessionToken : "";
        String persona = normalize(snippet);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(persona).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String synopsis = resolved.toString();
        Files.write(Paths.get(synopsis), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
