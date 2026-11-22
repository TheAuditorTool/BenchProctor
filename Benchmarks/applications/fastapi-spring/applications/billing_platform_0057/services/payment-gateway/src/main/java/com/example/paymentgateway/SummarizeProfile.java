// SPDX-License-Identifier: Apache-2.0
package com.example.paymentgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SummarizeProfile {


    @GetMapping("/SummarizeProfile/{pathId}")
    public void summarizeProfile(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = pathId;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(caption, "json");
        String remittance = entry.getKey();
        new ProcessBuilder("echo", remittance).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
