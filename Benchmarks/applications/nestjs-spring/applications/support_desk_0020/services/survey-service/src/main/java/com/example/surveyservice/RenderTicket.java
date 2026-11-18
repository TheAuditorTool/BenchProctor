// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderTicket {


    @GetMapping("/RenderTicket")
    public void renderTicket(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = referer != null ? referer : "";
        String inquiry = phrase.isEmpty() ? "default" : phrase;
        String content = Files.readString(Paths.get("/var/app/data/" + inquiry), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
