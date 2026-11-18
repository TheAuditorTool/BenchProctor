// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class VerifyIndex {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }
    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/VerifyIndex")
    public void verifyIndex(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = req.payload;
        String grievance = normalize(subject);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(grievance).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String verdict = resolved.toString();
        Files.write(Paths.get(verdict), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
