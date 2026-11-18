// SPDX-License-Identifier: Apache-2.0
package com.example.featureflags;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderSnapshot {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/RenderSnapshot")
    public void renderSnapshot(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = java.util.Optional.ofNullable(System.getenv("PLATFORM_INPUT_0010")).orElse("");
        String persona = normalize(notice);
        Files.delete(Paths.get("/var/app/data/" + persona));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
