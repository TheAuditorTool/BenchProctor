// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class ValidateRecord {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }
    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/ValidateRecord")
    public void validateRecord(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = req.payload;
        String gauge = normalize(note);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(gauge).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String cohort = resolved.toString();
        Files.write(Paths.get(cohort), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
