// SPDX-License-Identifier: Apache-2.0
package com.example.canarycontroller;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class SummarizeReport {


    @GetMapping("/SummarizeReport")
    public void summarizeReport(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = userAgent != null ? userAgent : "";
        String prefix = remark.length() > 0 ? remark.substring(0, 1).toLowerCase() : "";
        String note;
        switch (prefix) {
            case "h": note = remark.toLowerCase(); break;
            case "f": note = remark.toUpperCase(); break;
            default: note = remark.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(note.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
