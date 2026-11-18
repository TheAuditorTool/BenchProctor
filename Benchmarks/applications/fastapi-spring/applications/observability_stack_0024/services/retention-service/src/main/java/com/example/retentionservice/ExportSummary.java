// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportSummary {


    @GetMapping("/ExportSummary")
    public void exportSummary(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0024")).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(summary, "http");
        String cohort = edge.getKey();
        new ProcessBuilder("echo", cohort).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
