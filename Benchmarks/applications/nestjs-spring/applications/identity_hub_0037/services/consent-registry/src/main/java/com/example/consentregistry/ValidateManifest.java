// SPDX-License-Identifier: Apache-2.0
package com.example.consentregistry;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateManifest {


    @GetMapping("/ValidateManifest")
    public void validateManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = origin != null ? origin : "";
        String persona = remark.isEmpty() ? "default" : remark;
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = objectMapper.readTree(persona);
        response.getWriter().print(node.path("name").asText());
    }
}
