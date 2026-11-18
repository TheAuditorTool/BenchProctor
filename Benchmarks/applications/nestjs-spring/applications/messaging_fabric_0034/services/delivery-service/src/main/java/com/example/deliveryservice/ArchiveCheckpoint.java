// SPDX-License-Identifier: Apache-2.0
package com.example.deliveryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class ArchiveCheckpoint {


    @GetMapping("/ArchiveCheckpoint")
    public void archiveCheckpoint(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(System.getenv("MESSAGING_INPUT_0034")).orElse("");
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String bulletin;
        switch (prefix) {
            case "h": bulletin = footnote.toLowerCase(); break;
            case "f": bulletin = footnote.toUpperCase(); break;
            default: bulletin = footnote.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(bulletin);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
