// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class SearchKnowledge {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("support_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SearchKnowledge")
    public void searchKnowledge(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = inboundPayload.value != null ? inboundPayload.value : "";
        String content = Files.readString(Paths.get("/var/app/data/" + excerpt), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
