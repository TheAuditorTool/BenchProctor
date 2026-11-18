// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class IndexMetadata {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("media_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/IndexMetadata")
    public void indexMetadata(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = inboundPayload.value != null ? inboundPayload.value : "";
        new ProcessBuilder("echo", paragraph).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
