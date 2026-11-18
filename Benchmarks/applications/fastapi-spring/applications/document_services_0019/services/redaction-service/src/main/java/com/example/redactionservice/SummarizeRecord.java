// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeRecord {


    @GetMapping("/SummarizeRecord")
    public void summarizeRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : passage.split(",")) { tokens.add(token.trim()); }
        String dossier = String.join(",", tokens);
        new ProcessBuilder("echo", dossier).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
