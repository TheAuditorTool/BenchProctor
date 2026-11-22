// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class RotateDigest {


    @GetMapping("/RotateDigest")
    public void rotateDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = userAgent != null ? userAgent : "";
        String prefix = note.length() > 0 ? note.substring(0, 1).toLowerCase() : "";
        String cohort;
        switch (prefix) {
            case "h": cohort = note.toLowerCase(); break;
            case "f": cohort = note.toUpperCase(); break;
            default: cohort = note.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(cohort.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
