// SPDX-License-Identifier: Apache-2.0
package com.example.refundservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactDigest {


    @GetMapping("/CompactDigest/{pathId}")
    public void compactDigest(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = pathId;
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(headline, "form");
        String remittance = pair.getKey();
        new ProcessBuilder("echo", remittance).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
