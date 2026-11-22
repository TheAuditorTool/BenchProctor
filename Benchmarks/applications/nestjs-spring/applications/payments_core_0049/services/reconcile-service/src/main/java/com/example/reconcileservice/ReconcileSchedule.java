// SPDX-License-Identifier: Apache-2.0
package com.example.reconcileservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileSchedule {


    @PostMapping(path="/ReconcileSchedule", consumes="text/plain")
    public void reconcileSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = rawBody != null ? rawBody : "";
        String disbursement;
        if (headline.length() > 256) { disbursement = headline.substring(0, 256); }
        else { disbursement = headline; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(disbursement)) { response.sendError(403); return; }
        String remittance = disbursement;
        Runtime.getRuntime().exec(new String[]{remittance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
