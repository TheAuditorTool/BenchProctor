// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class ValidateComment {


    @GetMapping("/ValidateComment")
    public void validateComment(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = userAgent != null ? userAgent : "";
        String prefix = caption.length() > 0 ? caption.substring(0, 1).toLowerCase() : "";
        String synopsis;
        switch (prefix) {
            case "h": synopsis = caption.toLowerCase(); break;
            case "f": synopsis = caption.toUpperCase(); break;
            default: synopsis = caption.strip(); break;
        }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = objectMapper.readValue(synopsis.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
