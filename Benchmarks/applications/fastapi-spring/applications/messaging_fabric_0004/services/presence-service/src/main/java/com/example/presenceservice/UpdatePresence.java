// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class UpdatePresence {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("messaging_payload")
        public String value;
        public InboundPayload() {}
    }
    private static String escapeHtml(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#39;");
    }

    @PostMapping("/UpdatePresence")
    public void updatePresence(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print(escapeHtml(transcript));
    }
}
