// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactIndex {


    @GetMapping("/CompactIndex")
    public void compactIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = userAgent != null ? userAgent : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(transcript.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String backorder = String.join(",", lowered);
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(backorder);
        response.getWriter().print(node.path("name").asText());
    }
}
