// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ResolveReceipt {


    @GetMapping("/ResolveReceipt")
    public void resolveReceipt(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = authorization != null ? authorization : "";
        String rendition = citation.isEmpty() ? "default" : citation;
        java.net.URI parsed = java.net.URI.create(rendition);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String montage = rendition;
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(montage);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
