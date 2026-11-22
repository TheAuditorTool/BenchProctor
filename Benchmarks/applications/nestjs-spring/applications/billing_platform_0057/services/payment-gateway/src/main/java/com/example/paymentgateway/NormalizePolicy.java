// SPDX-License-Identifier: Apache-2.0
package com.example.paymentgateway;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizePolicy {


    @PostMapping(path="/NormalizePolicy", consumes="text/plain")
    public void normalizePolicy(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = rawBody != null ? rawBody : "";
        String remittance;
        if (caption.length() > 256) { remittance = caption.substring(0, 256); }
        else { remittance = caption; }
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(remittance)) { response.sendError(403); return; }
        String dunning = remittance;
        Runtime.getRuntime().exec(new String[]{dunning}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
