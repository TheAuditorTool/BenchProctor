// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class PruneCheckpoint {


    @GetMapping("/PruneCheckpoint")
    public void pruneCheckpoint(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = java.util.Optional.ofNullable(System.getenv("TELEMETRY_INPUT_0043")).orElse("");
        String prefix = note.length() > 0 ? note.substring(0, 1).toLowerCase() : "";
        String gauge;
        switch (prefix) {
            case "h": gauge = note.toLowerCase(); break;
            case "f": gauge = note.toUpperCase(); break;
            default: gauge = note.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(gauge);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
