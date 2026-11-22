// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateCheckpoint {


    @PostMapping(path="/ValidateCheckpoint", consumes="text/plain")
    public void validateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = rawBody != null ? rawBody : "";
        byte[] raw = synopsis.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String rendition = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String montage = rendition.matches("^(plain|markdown|html|text)$") ? rendition : "plain";
        response.getWriter().print("<div>" + montage + "</div>");
    }
}
