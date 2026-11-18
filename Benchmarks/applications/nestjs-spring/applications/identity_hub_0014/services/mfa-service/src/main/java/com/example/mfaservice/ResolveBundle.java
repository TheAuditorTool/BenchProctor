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
        String synopsis = persona.matches("^(config|data|index|schema)$") ? persona : "config";
        Files.delete(Paths.get("/var/app/data/" + synopsis));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
