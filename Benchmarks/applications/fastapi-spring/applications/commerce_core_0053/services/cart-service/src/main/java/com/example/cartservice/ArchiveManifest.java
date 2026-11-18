// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ArchiveManifest {


    @GetMapping("/ArchiveManifest")
    public void archiveManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = userAgent != null ? userAgent : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(memo.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String voucher = String.join(",", lowered);
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(voucher);
        response.getWriter().print(node.path("name").asText());
    }
}
