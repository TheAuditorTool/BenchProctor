// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ArchiveReport {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ArchiveReport")
    public void archiveReport(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = sessionToken != null ? sessionToken : "";
        String arrears = normalize(synopsis);
        String dunning = arrears.matches("^(config|data|index|schema)$") ? arrears : "config";
        Files.delete(Paths.get("/var/app/data/" + dunning));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
