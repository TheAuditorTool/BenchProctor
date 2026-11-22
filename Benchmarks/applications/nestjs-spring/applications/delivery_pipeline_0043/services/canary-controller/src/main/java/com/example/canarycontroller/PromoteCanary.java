// SPDX-License-Identifier: Apache-2.0
package com.example.canarycontroller;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PromoteCanary {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("delivery_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/PromoteCanary")
    public void promoteCanary(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = inboundPayload.value != null ? inboundPayload.value : "";
        String phrase = subject.matches("^(config|data|index|schema)$") ? subject : "config";
        Files.write(Paths.get("/var/uploads/" + phrase), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
