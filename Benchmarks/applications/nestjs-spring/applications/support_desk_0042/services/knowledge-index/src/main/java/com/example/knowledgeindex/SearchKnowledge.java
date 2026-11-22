// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class SearchKnowledge {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("support_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SearchKnowledge")
    public void searchKnowledge(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + note + "</div>");
    }
}
