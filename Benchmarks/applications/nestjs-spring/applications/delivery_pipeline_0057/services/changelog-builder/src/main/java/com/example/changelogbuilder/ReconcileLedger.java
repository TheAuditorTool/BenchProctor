// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ReconcileLedger {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ReconcileLedger")
    public void reconcileLedger(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = sessionToken != null ? sessionToken : "";
        String wording = normalize(footnote);
        String note = wording.matches("^(config|data|index|schema)$") ? wording : "config";
        Files.delete(Paths.get("/var/app/data/" + note));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
