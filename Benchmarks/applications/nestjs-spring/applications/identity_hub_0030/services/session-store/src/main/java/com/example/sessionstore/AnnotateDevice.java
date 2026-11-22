// SPDX-License-Identifier: Apache-2.0
package com.example.sessionstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateDevice {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/AnnotateDevice")
    public void annotateDevice(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = java.util.Optional.ofNullable(commentText).orElse("");
        String persona = normalize(tagline);
        java.net.URI parsed = java.net.URI.create(persona);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String note = persona;
        org.apache.hc.client5.http.classic.methods.HttpGet fetchRequest = new org.apache.hc.client5.http.classic.methods.HttpGet(note);
        try (org.apache.hc.client5.http.impl.classic.CloseableHttpClient fetchClient = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault()) {
            int fetchStatus = fetchClient.execute(fetchRequest, fetchResponse -> fetchResponse.getCode());
            response.setHeader("X-Fetch-Status", String.valueOf(fetchStatus));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
