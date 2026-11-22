// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class ExportBatch {


    @GetMapping("/ExportBatch")
    public void exportBatch(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = userAgent != null ? userAgent : "";
        String prefix = memo.length() > 0 ? memo.substring(0, 1).toLowerCase() : "";
        String verdict;
        switch (prefix) {
            case "h": verdict = memo.toLowerCase(); break;
            case "f": verdict = memo.toUpperCase(); break;
            default: verdict = memo.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(verdict.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
