// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class QuoteShipment {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("shipping_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/QuoteShipment")
    public void quoteShipment(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = inboundPayload.value != null ? inboundPayload.value : "";
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(footnote)) { response.sendError(403); return; }
        String consignment = "/var/app/data/" + footnote;
        String content = Files.readString(Paths.get(consignment), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
