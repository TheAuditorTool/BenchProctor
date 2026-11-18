// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LookupSku {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("inventory_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/LookupSku")
    public void lookupSku(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + memo + "</div>");
    }
}
