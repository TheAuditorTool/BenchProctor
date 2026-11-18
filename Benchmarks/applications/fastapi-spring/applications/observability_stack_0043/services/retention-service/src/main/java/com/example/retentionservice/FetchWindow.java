// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchWindow {


    @GetMapping("/FetchWindow")
    public void fetchWindow(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0043")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(note, "query");
        String gauge = kv.getKey();
        new ProcessBuilder("echo", gauge).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
