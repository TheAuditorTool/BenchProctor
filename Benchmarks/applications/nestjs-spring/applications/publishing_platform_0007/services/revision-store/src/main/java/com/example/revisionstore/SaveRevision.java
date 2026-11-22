// SPDX-License-Identifier: Apache-2.0
package com.example.revisionstore;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class SaveRevision {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("publishing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SaveRevision")
    public void saveRevision(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = inboundPayload.value != null ? inboundPayload.value : "";
        if (!transcript.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { response.sendError(400); return; }
        Files.write(Paths.get("/var/uploads/" + transcript), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
