// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PostLedgerEntry {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("billing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/PostLedgerEntry")
    public void postLedgerEntry(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remittance = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + remittance + "</div>");
    }
}
