// SPDX-License-Identifier: Apache-2.0
package com.example.canarycontroller;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PruneReport {


    @PostMapping(path="/PruneReport", consumes="application/xml")
    public void pruneReport(@javax.validation.constraints.Size(max = 4096) @RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = xmlBody;
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> remark.strip().toLowerCase())
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip());
        String note = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(note);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
