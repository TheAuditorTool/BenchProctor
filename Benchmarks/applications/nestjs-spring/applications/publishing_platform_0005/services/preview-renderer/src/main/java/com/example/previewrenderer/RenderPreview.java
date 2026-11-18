// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderPreview {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("publishing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RenderPreview")
    public void renderPreview(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + paragraph + "</div>");
    }
}
