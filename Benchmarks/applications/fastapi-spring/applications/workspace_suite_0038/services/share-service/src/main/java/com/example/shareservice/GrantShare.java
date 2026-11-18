// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class GrantShare {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("workspace_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/GrantShare")
    public void grantShare(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = inboundPayload.value != null ? inboundPayload.value : "";
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(notice).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String wording = resolved.toString();
        Files.write(Paths.get(wording), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
