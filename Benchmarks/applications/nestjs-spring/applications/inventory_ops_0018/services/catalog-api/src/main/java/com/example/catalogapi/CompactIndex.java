// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class CompactIndex {


    @GetMapping("/CompactIndex")
    public void compactIndex(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = java.util.Optional.ofNullable(System.getenv("INVENTORY_INPUT_0018")).orElse("");
        String prefix = transcript.length() > 0 ? transcript.substring(0, 1).toLowerCase() : "";
        String backorder;
        switch (prefix) {
            case "h": backorder = transcript.toLowerCase(); break;
            case "f": backorder = transcript.toUpperCase(); break;
            default: backorder = transcript.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(backorder);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
