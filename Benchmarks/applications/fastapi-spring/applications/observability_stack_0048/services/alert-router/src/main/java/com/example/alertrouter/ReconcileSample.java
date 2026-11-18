// SPDX-License-Identifier: Apache-2.0
package com.example.alertrouter;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileSample {


    @GetMapping("/ReconcileSample")
    public void reconcileSample(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0048")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(excerpt, "http");
        String gauge = kv.getKey();
        new ProcessBuilder("echo", gauge).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
