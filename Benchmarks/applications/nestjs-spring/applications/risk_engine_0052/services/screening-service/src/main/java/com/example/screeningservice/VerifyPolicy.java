// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.validation.Valid;

@RestController
class VerifyPolicy {

    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/VerifyPolicy")
    public void verifyPolicy(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : memo.split(",")) { tokens.add(token.trim()); }
        String verdict = String.join(",", tokens);
        String grievance = verdict.matches("^(config|data|index|schema)$") ? verdict : "config";
        Files.delete(Paths.get("/var/app/data/" + grievance));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
