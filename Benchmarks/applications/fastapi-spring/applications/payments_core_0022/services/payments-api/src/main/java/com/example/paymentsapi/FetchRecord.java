// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchRecord {


    @GetMapping("/FetchRecord")
    public void fetchRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : subject.split(",")) { tokens.add(token.trim()); }
        String ledger = String.join(",", tokens);
        new ProcessBuilder("echo", ledger).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
