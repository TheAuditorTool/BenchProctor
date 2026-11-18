// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateTenant {


    @GetMapping("/ValidateTenant")
    public void validateTenant(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = java.util.Optional.ofNullable(System.getenv("PLATFORM_INPUT_0001")).orElse("");
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(tagline, "json");
        String persona = tuple.getKey();
        new ProcessBuilder("echo", persona).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
