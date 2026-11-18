// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class ApplyRedaction {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("documents_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/ApplyRedaction")
    public void applyRedaction(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = inboundPayload.value != null ? inboundPayload.value : "";
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(transcript);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
