// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatHeader {


    @GetMapping("/FormatHeader")
    public void formatHeader(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = authorization != null ? authorization : "";
        java.util.function.Supplier<String> valueSupplier = () -> caption.strip();
        String gauge = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + gauge}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
