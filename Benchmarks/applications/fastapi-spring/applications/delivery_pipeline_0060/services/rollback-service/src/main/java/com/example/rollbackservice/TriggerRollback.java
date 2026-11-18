// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class TriggerRollback {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("delivery_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/TriggerRollback")
    public void triggerRollback(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subtitle = inboundPayload.value != null ? inboundPayload.value : "";
        Files.write(Paths.get("/var/uploads/" + subtitle), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
