// SPDX-License-Identifier: Apache-2.0
package com.example.allocationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class SolveAllocation {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("inventory_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SolveAllocation")
    public void solveAllocation(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + headline + "</div>");
    }
}
