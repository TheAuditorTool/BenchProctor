// SPDX-License-Identifier: Apache-2.0
package com.example.watchlistsync;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ExportRule {


    @GetMapping("/ExportRule")
    public void exportRule(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = origin != null ? origin : "";
        String verdict = excerpt.isEmpty() ? "default" : excerpt;
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = objectMapper.readTree(verdict);
        response.getWriter().print(node.path("name").asText());
    }
}
