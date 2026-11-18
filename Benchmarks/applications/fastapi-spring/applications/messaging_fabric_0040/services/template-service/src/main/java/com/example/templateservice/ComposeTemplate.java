// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class ComposeTemplate {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("messaging_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ComposeTemplate")
    public void composeTemplate(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = inboundPayload.value != null ? inboundPayload.value : "";
        String socketRaw = String.valueOf(phrase);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
