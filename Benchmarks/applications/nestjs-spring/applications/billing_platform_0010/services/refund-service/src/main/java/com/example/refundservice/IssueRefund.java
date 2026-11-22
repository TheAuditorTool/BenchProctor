// SPDX-License-Identifier: Apache-2.0
package com.example.refundservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class IssueRefund {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("billing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/IssueRefund")
    public void issueRefund(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String arrears = inboundPayload.value != null ? inboundPayload.value : "";
        String content = Files.readString(Paths.get("/var/app/data/" + arrears), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
