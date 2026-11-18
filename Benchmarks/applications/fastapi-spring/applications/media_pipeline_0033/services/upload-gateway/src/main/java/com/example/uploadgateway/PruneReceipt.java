// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneReceipt {


    @GetMapping("/PruneReceipt")
    public void pruneReceipt(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = java.util.Optional.ofNullable(System.getenv("MEDIA_INPUT_0033")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(transcript, "json");
        String rendition = kv.getKey();
        new ProcessBuilder("echo", rendition).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
