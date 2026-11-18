// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class IngestMetric {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("telemetry_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/IngestMetric")
    public void ingestMetric(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = inboundPayload.value != null ? inboundPayload.value : "";
        Files.delete(Paths.get("/var/app/data/" + heading));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
