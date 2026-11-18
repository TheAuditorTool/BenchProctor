// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ResolveIndex {


    @GetMapping("/ResolveIndex")
    public void resolveIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> snippet.strip();
        String persona = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + persona}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
