// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LookupOrder {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("orders_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/LookupOrder")
    public void lookupOrder(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = inboundPayload.value != null ? inboundPayload.value : "";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + summary});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
