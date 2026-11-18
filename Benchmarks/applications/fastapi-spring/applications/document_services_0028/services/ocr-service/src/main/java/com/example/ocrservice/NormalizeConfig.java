// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class NormalizeConfig {


    @GetMapping("/NormalizeConfig")
    public void normalizeConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = xForwardedFor != null ? xForwardedFor : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : note.split(",")) { tokens.add(token.trim()); }
        String addendum = String.join(",", tokens);
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(addendum.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        response.getWriter().print(deserialized);
    }
}
