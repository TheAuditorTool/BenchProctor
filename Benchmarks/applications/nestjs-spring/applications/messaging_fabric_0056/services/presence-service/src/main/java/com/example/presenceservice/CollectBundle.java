// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CollectBundle {


    @GetMapping("/CollectBundle")
    public void collectBundle(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = host != null ? host : "";
        String bulletin = footnote.isEmpty() ? "default" : footnote;
        String snippet = bulletin.matches("^(config|data|index|schema)$") ? bulletin : "config";
        Files.write(Paths.get("/var/uploads/" + snippet), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
