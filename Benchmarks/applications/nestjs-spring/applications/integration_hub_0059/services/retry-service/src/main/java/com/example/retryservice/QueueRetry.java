// SPDX-License-Identifier: Apache-2.0
package com.example.retryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class QueueRetry {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("integrations_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/QueueRetry")
    public void queueRetry(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + remark + "</div>");
    }
}
