// SPDX-License-Identifier: Apache-2.0
package com.example.deliveryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactProfile {


    @GetMapping("/CompactProfile")
    public void compactProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> preface.strip();
        String bulletin = valueSupplier.get();
        new ProcessBuilder("echo", bulletin).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
