// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class BuildManifest {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("shipping_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/BuildManifest")
    public void buildManifest(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = inboundPayload.value != null ? inboundPayload.value : "";
        Files.delete(Paths.get("/var/app/data/" + footnote));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
