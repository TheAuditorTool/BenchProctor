// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PruneRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/PruneRoster")
    public void pruneRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(preface);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(bulletin).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String notice = resolved.toString();
        Files.write(Paths.get(notice), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
