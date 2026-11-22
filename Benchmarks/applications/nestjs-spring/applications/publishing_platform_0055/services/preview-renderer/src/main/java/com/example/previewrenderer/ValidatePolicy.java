// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidatePolicy {


    @GetMapping("/ValidatePolicy")
    public void validatePolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> synopsis.strip();
        String byline = valueSupplier.get();
        new ProcessBuilder("echo", byline).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
