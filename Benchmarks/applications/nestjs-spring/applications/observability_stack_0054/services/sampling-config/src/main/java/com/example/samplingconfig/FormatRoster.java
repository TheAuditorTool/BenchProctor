// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatRoster {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/FormatRoster")
    public void formatRoster(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = host != null ? host : "";
        String cohort = normalize(excerpt);
        java.net.URI parsed = java.net.URI.create(cohort);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String gauge = cohort;
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(gauge);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
