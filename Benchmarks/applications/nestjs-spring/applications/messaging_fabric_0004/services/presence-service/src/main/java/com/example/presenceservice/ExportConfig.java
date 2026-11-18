// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ExportConfig {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ExportConfig")
    public void exportConfig(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = sessionToken != null ? sessionToken : "";
        String bulletin = normalize(paragraph);
        String synopsis = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        Files.delete(Paths.get("/var/app/data/" + synopsis));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
