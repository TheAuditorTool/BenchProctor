// SPDX-License-Identifier: Apache-2.0
package com.example.labelservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class BuildHeader {


    @GetMapping("/BuildHeader")
    public void buildHeader(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(System.getenv("SHIPPING_INPUT_0037")).orElse("");
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String consignment;
        switch (prefix) {
            case "h": consignment = footnote.toLowerCase(); break;
            case "f": consignment = footnote.toUpperCase(); break;
            default: consignment = footnote.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(consignment);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
