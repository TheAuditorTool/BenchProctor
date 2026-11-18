// SPDX-License-Identifier: Apache-2.0
package com.example.configservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RolloutConfig {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("platform_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RolloutConfig")
    public void rolloutConfig(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + preface + "</div>");
    }
}
