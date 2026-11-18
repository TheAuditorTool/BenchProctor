// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class TrackPresence {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("workspace_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/TrackPresence")
    public void trackPresence(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + transcript + "</div>");
    }
}
