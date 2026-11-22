// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.validation.Valid;

@RestController
class SummarizeCheckpoint {

    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/SummarizeCheckpoint")
    public void summarizeCheckpoint(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String inquiry = String.join(",", tokens);
        String grievance = inquiry.matches("^(config|data|index|schema)$") ? inquiry : "config";
        Files.delete(Paths.get("/var/app/data/" + grievance));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
