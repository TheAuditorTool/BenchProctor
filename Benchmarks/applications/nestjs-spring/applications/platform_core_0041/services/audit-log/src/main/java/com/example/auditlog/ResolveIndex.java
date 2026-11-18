// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveIndex {


    @GetMapping("/ResolveIndex")
    public void resolveIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = referer != null ? referer : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String persona = transform.apply(passage);
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(persona).normalize();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String handshake = resolved.toString();
        Files.write(Paths.get(handshake), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
