// SPDX-License-Identifier: Apache-2.0
package com.example.documentapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class UploadDocument {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("documents_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/UploadDocument")
    public void uploadDocument(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = inboundPayload.value != null ? inboundPayload.value : "";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + transcript}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
