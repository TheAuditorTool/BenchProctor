// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CollectSummary {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/CollectSummary")
    public void collectSummary(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(preface);
        String notice = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        Files.delete(Paths.get("/var/app/data/" + notice));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
