// SPDX-License-Identifier: Apache-2.0
package com.example.allocationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ResolveRoster")
    public void resolveRoster(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = sessionToken != null ? sessionToken : "";
        String restock = normalize(summary);
        String backorder = restock.matches("^(config|data|index|schema)$") ? restock : "config";
        Files.delete(Paths.get("/var/app/data/" + backorder));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
