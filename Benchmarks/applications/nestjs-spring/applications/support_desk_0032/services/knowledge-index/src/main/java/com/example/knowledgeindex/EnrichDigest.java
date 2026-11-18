// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class EnrichDigest {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/EnrichDigest")
    public void enrichDigest(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = sessionToken != null ? sessionToken : "";
        String inquiry = normalize(note);
        String grievance = inquiry.matches("^(config|data|index|schema)$") ? inquiry : "config";
        Files.delete(Paths.get("/var/app/data/" + grievance));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
