// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderAttachment {


    @GetMapping("/RenderAttachment")
    public void renderAttachment(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = java.util.Optional.ofNullable(System.getenv("DOCUMENTS_INPUT_0028")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(note, "header");
        String addendum = kv.getKey();
        new ProcessBuilder("echo", addendum).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
