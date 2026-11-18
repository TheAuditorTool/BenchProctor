// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class SummarizeRelease {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/SummarizeRelease")
    public void summarizeRelease(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = sessionToken != null ? sessionToken : "";
        String remark = normalize(wording);
        String phrase = remark.matches("^(config|data|index|schema)$") ? remark : "config";
        Files.delete(Paths.get("/var/app/data/" + phrase));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
