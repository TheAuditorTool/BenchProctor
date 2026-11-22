// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.validation.Valid;

@RestController
class NormalizeFlag {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/NormalizeFlag")
    public void normalizeFlag(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subtitle = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : subtitle.split(",")) { tokens.add(token.trim()); }
        String persona = String.join(",", tokens);
        String handshake = persona.matches("^(config|data|index|schema)$") ? persona : "config";
        Files.delete(Paths.get("/var/app/data/" + handshake));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
