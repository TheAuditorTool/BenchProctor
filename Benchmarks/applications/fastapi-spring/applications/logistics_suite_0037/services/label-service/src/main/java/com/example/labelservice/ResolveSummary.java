// SPDX-License-Identifier: Apache-2.0
package com.example.labelservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ResolveSummary {


    @GetMapping("/ResolveSummary")
    public void resolveSummary(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : footnote.split(",")) { tokens.add(token.trim()); }
        String consignment = String.join(",", tokens);
        new ProcessBuilder("echo", consignment).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
