// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RecordBounce {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("messaging_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RecordBounce")
    public void recordBounce(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + note + "</div>");
    }
}
