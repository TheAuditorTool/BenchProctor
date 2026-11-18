// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatDigest {


    @GetMapping("/FormatDigest")
    public void formatDigest(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = java.util.Optional.ofNullable(System.getenv("INVENTORY_INPUT_0016")).orElse("");
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(citation, "http");
        String backorder = tuple.getKey();
        new ProcessBuilder("echo", backorder).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
