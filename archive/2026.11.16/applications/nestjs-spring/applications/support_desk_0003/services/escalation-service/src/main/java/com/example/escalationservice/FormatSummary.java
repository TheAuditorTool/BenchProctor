// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FormatSummary {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/FormatSummary")
    public void formatSummary(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = java.util.Optional.ofNullable(System.getenv("SUPPORT_INPUT_0003")).orElse("");
        String grievance = normalize(citation);
        Files.delete(Paths.get("/var/app/data/" + grievance));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
