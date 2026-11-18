// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactRoster {


    @GetMapping("/CompactRoster")
    public void compactRoster(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("RISK_INPUT_0030")).orElse("");
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(summary, "body");
        String grievance = pair.getKey();
        new ProcessBuilder("echo", grievance).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
