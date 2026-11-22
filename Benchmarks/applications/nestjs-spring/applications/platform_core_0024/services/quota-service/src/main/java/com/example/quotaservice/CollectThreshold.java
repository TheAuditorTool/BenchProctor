// SPDX-License-Identifier: Apache-2.0
package com.example.quotaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class CollectThreshold {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/CollectThreshold")
    public void collectThreshold(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : heading.split(",")) { tokens.add(token.trim()); }
        String handshake = String.join(",", tokens);
        String persona = handshake.matches("^(config|data|index|schema)$") ? handshake : "config";
        Files.delete(Paths.get("/var/app/data/" + persona));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
