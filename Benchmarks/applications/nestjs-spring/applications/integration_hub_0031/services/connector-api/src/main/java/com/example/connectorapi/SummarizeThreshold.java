// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class SummarizeThreshold {


    @GetMapping("/SummarizeThreshold")
    public void summarizeThreshold(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = java.util.Optional.ofNullable(System.getenv("INTEGRATIONS_INPUT_0031")).orElse("");
        String prefix = snippet.length() > 0 ? snippet.substring(0, 1).toLowerCase() : "";
        String handshake;
        switch (prefix) {
            case "h": handshake = snippet.toLowerCase(); break;
            case "f": handshake = snippet.toUpperCase(); break;
            default: handshake = snippet.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(handshake);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
