// SPDX-License-Identifier: Apache-2.0
package com.example.reconcileservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class NormalizeIndex {


    @GetMapping("/NormalizeIndex")
    public void normalizeIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> headline.strip();
        String disbursement = valueSupplier.get();
        ProcessBuilder interpreterJob = new ProcessBuilder().redirectErrorStream(true);
        interpreterJob.command("/bin/bash", "-c", "ping -c 1 -- " + disbursement);
        interpreterJob.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
