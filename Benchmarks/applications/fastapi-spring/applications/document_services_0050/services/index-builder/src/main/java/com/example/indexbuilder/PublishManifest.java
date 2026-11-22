// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class PublishManifest {


    @GetMapping("/PublishManifest")
    public void publishManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = userAgent != null ? userAgent : "";
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String dossier;
        switch (prefix) {
            case "h": dossier = citation.toLowerCase(); break;
            case "f": dossier = citation.toUpperCase(); break;
            default: dossier = citation.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(dossier.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
