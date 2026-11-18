// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FetchBundle {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/FetchBundle")
    public void fetchBundle(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(subject);
        String passage = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        Files.delete(Paths.get("/var/app/data/" + passage));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
