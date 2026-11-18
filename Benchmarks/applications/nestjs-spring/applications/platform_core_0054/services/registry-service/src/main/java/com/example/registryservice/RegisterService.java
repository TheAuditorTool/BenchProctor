// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class RegisterService {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("platform_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RegisterService")
    public void registerService(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = inboundPayload.value != null ? inboundPayload.value : "";
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(caption);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
