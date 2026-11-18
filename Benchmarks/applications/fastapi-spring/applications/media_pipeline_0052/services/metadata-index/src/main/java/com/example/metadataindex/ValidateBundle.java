// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateBundle {


    @GetMapping("/ValidateBundle")
    public void validateBundle(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = java.util.Optional.ofNullable(System.getenv("MEDIA_INPUT_0052")).orElse("");
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(tagline, "header");
        String rendition = entry.getKey();
        new ProcessBuilder("echo", rendition).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
