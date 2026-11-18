// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class FetchConfig {


    @GetMapping("/FetchConfig")
    public void fetchConfig(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = java.util.Optional.ofNullable(System.getenv("DOCUMENTS_INPUT_0019")).orElse("");
        String prefix = passage.length() > 0 ? passage.substring(0, 1).toLowerCase() : "";
        String dossier;
        switch (prefix) {
            case "h": dossier = passage.toLowerCase(); break;
            case "f": dossier = passage.toUpperCase(); break;
            default: dossier = passage.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(dossier);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
