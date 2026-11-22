// SPDX-License-Identifier: Apache-2.0
package com.example.dunningservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class EnrichSummary {


    @GetMapping("/EnrichSummary")
    public void enrichSummary(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> footnote.strip();
        String remittance = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + remittance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
