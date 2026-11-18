// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderMacro {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/RenderMacro")
    public void renderMacro(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(System.getenv("SUPPORT_INPUT_0005")).orElse("");
        String inquiry = normalize(phrase);
        Files.delete(Paths.get("/var/app/data/" + inquiry));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
