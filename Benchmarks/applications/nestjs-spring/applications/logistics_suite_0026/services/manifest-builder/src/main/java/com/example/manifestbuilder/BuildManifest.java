// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class BuildManifest {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("shipping_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/BuildManifest")
    public void buildManifest(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = inboundPayload.value != null ? inboundPayload.value : "";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + preface}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
