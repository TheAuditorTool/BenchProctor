// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class BuildChangelog {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("delivery_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/BuildChangelog")
    public void buildChangelog(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = inboundPayload.value != null ? inboundPayload.value : "";
        byte[] serBytes = java.util.Base64.getDecoder().decode(tagline);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
