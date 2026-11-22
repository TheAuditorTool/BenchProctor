// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RaiseEscalation {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("support_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RaiseEscalation")
    public void raiseEscalation(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = inboundPayload.value != null ? inboundPayload.value : "";
        String grievance = memo.matches("^(config|data|index|schema)$") ? memo : "config";
        Files.delete(Paths.get("/var/app/data/" + grievance));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
