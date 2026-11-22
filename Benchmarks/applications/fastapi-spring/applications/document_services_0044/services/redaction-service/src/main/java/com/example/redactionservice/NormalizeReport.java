// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class NormalizeReport {


    @GetMapping("/NormalizeReport")
    public void normalizeReport(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = userAgent != null ? userAgent : "";
        String prefix = phrase.length() > 0 ? phrase.substring(0, 1).toLowerCase() : "";
        String dossier;
        switch (prefix) {
            case "h": dossier = phrase.toLowerCase(); break;
            case "f": dossier = phrase.toUpperCase(); break;
            default: dossier = phrase.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(dossier.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
