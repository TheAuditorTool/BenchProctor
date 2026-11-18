// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuthorizePayment {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("payments_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/AuthorizePayment")
    public void authorizePayment(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String disbursement = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
