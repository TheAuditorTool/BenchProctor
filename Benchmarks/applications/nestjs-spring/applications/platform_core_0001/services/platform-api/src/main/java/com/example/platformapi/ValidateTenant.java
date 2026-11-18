// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class ValidateTenant {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }
    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/ValidateTenant")
    public void validateTenant(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = req.payload;
        String persona = normalize(tagline);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(persona).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String handshake = resolved.toString();
        Files.write(Paths.get(handshake), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
