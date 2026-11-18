// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class ValidateSnapshot {


    @GetMapping("/ValidateSnapshot")
    public void validateSnapshot(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("MESSAGING_INPUT_0013")).orElse("");
        String prefix = summary.length() > 0 ? summary.substring(0, 1).toLowerCase() : "";
        String bulletin;
        switch (prefix) {
            case "h": bulletin = summary.toLowerCase(); break;
            case "f": bulletin = summary.toUpperCase(); break;
            default: bulletin = summary.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(bulletin);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
