// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishCheckpoint {


    @GetMapping("/PublishCheckpoint")
    public void publishCheckpoint(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0011")).orElse("");
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(caption, "query");
        String gauge = tuple.getKey();
        new ProcessBuilder("echo", gauge).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
