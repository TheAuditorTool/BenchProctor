// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RunSettlement {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("billing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RunSettlement")
    public void runSettlement(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dunning = inboundPayload.value != null ? inboundPayload.value : "";
        if (!dunning.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + dunning + "</div>");
    }
}
