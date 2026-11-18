// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ProvisionTenant {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("platform_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ProvisionTenant")
    public void provisionTenant(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = inboundPayload.value != null ? inboundPayload.value : "";
        if (!wording.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + wording + "</div>");
    }
}
