// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeRoster {


    @GetMapping("/MergeRoster")
    public void mergeRoster(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = java.util.Optional.ofNullable(System.getenv("RISK_INPUT_0008")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(synopsis, "http");
        String verdict = kv.getKey();
        new ProcessBuilder("echo", verdict).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
