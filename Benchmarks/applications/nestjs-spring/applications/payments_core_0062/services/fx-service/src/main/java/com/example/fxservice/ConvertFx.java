// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ConvertFx {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("payments_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ConvertFx")
    public void convertFx(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String ledger = inboundPayload.value != null ? inboundPayload.value : "";
        Files.write(Paths.get("/var/uploads/" + ledger), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
