// SPDX-License-Identifier: Apache-2.0
package com.example.consentregistry;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PrunePolicy {


    @GetMapping("/PrunePolicy")
    public void prunePolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> remark.strip();
        String persona = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + persona}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
