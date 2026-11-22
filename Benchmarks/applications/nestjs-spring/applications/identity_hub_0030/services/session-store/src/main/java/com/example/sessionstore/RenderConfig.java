// SPDX-License-Identifier: Apache-2.0
package com.example.sessionstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderConfig {


    @GetMapping("/RenderConfig")
    public void renderConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = host != null ? host : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : tagline.split(",")) { tokens.add(token.trim()); }
        String persona = String.join(",", tokens);
        Files.write(Paths.get("/var/uploads/" + persona), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
