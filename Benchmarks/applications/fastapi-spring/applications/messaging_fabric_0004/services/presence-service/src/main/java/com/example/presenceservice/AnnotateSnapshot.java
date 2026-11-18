// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateSnapshot {


    @GetMapping("/AnnotateSnapshot")
    public void annotateSnapshot(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = java.util.Optional.ofNullable(System.getenv("MESSAGING_INPUT_0004")).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(paragraph, "header");
        String bulletin = edge.getKey();
        new ProcessBuilder("echo", bulletin).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
