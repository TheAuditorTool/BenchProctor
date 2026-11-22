// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class MergeIndex {


    @GetMapping("/MergeIndex")
    public void mergeIndex(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = origin != null ? origin : "";
        String ledger = memo.isEmpty() ? "default" : memo;
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = objectMapper.readTree(ledger);
        response.getWriter().print(node.path("name").asText());
    }
}
