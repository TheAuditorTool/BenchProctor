// SPDX-License-Identifier: Apache-2.0
package com.example.documentcollab;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class LoadRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/LoadRoster")
    public void loadRoster(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("WORKSPACE_INPUT_0007")).orElse("");
        String subtitle = normalize(summary);
        Files.delete(Paths.get("/var/app/data/" + subtitle));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
