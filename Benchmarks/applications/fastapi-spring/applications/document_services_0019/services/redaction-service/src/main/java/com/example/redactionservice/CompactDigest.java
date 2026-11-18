// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactDigest {


    @GetMapping("/CompactDigest")
    public void compactDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> passage.strip();
        String dossier = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + dossier}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
