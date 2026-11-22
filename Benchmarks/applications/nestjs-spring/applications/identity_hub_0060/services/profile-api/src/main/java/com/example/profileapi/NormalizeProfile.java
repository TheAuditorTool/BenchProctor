// SPDX-License-Identifier: Apache-2.0
package com.example.profileapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class NormalizeProfile {


    @GetMapping("/NormalizeProfile")
    public void normalizeProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> paragraph.strip();
        String persona = valueSupplier.get();
        new ProcessBuilder("echo", persona).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
