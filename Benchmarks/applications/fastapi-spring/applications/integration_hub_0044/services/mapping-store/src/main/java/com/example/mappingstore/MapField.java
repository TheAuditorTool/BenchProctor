// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MapField {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("integrations_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/MapField")
    public void mapField(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = inboundPayload.value != null ? inboundPayload.value : "";
        String citation = headline.matches("^(plain|markdown|html|text)$") ? headline : "plain";
        response.getWriter().print("<div>" + citation + "</div>");
    }
}
