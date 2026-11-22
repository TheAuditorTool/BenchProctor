// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class NormalizeRecord {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/NormalizeRecord")
    public void normalizeRecord(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : caption.split(",")) { tokens.add(token.trim()); }
        String synopsis = String.join(",", tokens);
        String snippet = synopsis.matches("^(config|data|index|schema)$") ? synopsis : "config";
        Files.delete(Paths.get("/var/app/data/" + snippet));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
