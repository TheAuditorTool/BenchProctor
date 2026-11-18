// SPDX-License-Identifier: Apache-2.0
package com.example.labelservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CreateLabel {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("shipping_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/CreateLabel")
    public void createLabel(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = inboundPayload.value != null ? inboundPayload.value : "";
        String content = Files.readString(Paths.get("/var/app/data/" + memo), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
