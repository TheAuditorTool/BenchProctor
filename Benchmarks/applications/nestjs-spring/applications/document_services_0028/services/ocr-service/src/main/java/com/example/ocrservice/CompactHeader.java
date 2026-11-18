// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class CompactHeader {


    @GetMapping("/CompactHeader")
    public void compactHeader(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = java.util.Optional.ofNullable(System.getenv("DOCUMENTS_INPUT_0028")).orElse("");
        String prefix = note.length() > 0 ? note.substring(0, 1).toLowerCase() : "";
        String addendum;
        switch (prefix) {
            case "h": addendum = note.toLowerCase(); break;
            case "f": addendum = note.toUpperCase(); break;
            default: addendum = note.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(addendum);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
