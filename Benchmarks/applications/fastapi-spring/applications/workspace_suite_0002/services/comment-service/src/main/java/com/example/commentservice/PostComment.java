// SPDX-License-Identifier: Apache-2.0
package com.example.commentservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PostComment {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("workspace_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/PostComment")
    public void postComment(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + summary + "</div>");
    }
}
