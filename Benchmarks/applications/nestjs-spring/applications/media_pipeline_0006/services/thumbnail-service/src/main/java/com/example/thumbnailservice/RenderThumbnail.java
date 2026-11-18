// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderThumbnail {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("media_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/RenderThumbnail")
    public void renderThumbnail(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = inboundPayload.value != null ? inboundPayload.value : "";
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(subject).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String rendition = resolved.toString();
        Files.write(Paths.get(rendition), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
