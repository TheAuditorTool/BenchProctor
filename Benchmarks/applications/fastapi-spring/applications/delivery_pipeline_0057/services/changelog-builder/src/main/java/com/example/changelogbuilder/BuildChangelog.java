// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class BuildChangelog {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("delivery_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/BuildChangelog")
    public void buildChangelog(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = inboundPayload.value != null ? inboundPayload.value : "";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + tagline}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
