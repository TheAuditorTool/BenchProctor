// SPDX-License-Identifier: Apache-2.0
package com.example.directorysync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class NormalizeSession {


    @GetMapping("/NormalizeSession")
    public void normalizeSession(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(System.getenv("IDENTITY_INPUT_0010")).orElse("");
        String prefix = phrase.length() > 0 ? phrase.substring(0, 1).toLowerCase() : "";
        String persona;
        switch (prefix) {
            case "h": persona = phrase.toLowerCase(); break;
            case "f": persona = phrase.toUpperCase(); break;
            default: persona = phrase.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(persona);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
