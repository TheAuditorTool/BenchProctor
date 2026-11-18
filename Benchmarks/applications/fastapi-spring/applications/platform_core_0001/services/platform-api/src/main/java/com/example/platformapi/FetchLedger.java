// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchLedger {


    @GetMapping("/FetchLedger")
    public void fetchLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = userAgent != null ? userAgent : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(tagline.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String persona = String.join(",", lowered);
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(persona);
        response.getWriter().print(node.path("name").asText());
    }
}
