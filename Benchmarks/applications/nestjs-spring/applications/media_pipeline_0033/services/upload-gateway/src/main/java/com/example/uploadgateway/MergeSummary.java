// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class MergeSummary {


    @GetMapping("/MergeSummary")
    public void mergeSummary(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = java.util.Optional.ofNullable(System.getenv("MEDIA_INPUT_0033")).orElse("");
        String prefix = transcript.length() > 0 ? transcript.substring(0, 1).toLowerCase() : "";
        String rendition;
        switch (prefix) {
            case "h": rendition = transcript.toLowerCase(); break;
            case "f": rendition = transcript.toUpperCase(); break;
            default: rendition = transcript.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(rendition);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
