// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class NormalizeConfig {


    @GetMapping("/NormalizeConfig")
    public void normalizeConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = xForwardedFor != null ? xForwardedFor : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : caption.split(",")) { tokens.add(token.trim()); }
        String gauge = String.join(",", tokens);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(gauge).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String cohort = resolved.toString();
        Files.write(Paths.get(cohort), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
