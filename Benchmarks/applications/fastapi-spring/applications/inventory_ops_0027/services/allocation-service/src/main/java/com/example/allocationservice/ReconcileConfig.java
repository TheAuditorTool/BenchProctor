// SPDX-License-Identifier: Apache-2.0
package com.example.allocationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileConfig {


    @GetMapping("/ReconcileConfig")
    public void reconcileConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : summary.split(",")) { tokens.add(token.trim()); }
        String restock = String.join(",", tokens);
        new ProcessBuilder("echo", restock).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
