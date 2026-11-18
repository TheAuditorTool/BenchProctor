// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneSummary {


    @GetMapping("/PruneSummary")
    public void pruneSummary(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = java.util.Optional.ofNullable(System.getenv("RISK_INPUT_0029")).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(subject, "cookie");
        String grievance = edge.getKey();
        new ProcessBuilder("echo", grievance).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
