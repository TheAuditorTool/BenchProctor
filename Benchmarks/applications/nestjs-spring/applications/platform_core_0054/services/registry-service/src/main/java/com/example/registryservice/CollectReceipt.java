// SPDX-License-Identifier: Apache-2.0
package com.example.registryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class CollectReceipt {


    @GetMapping("/CollectReceipt")
    public void collectReceipt(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = java.util.Optional.ofNullable(System.getenv("PLATFORM_INPUT_0054")).orElse("");
        String prefix = snippet.length() > 0 ? snippet.substring(0, 1).toLowerCase() : "";
        String persona;
        switch (prefix) {
            case "h": persona = snippet.toLowerCase(); break;
            case "f": persona = snippet.toUpperCase(); break;
            default: persona = snippet.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(persona);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
