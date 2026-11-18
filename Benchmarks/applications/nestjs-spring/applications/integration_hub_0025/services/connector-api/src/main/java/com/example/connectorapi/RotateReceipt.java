// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class RotateReceipt {


    @GetMapping("/RotateReceipt")
    public void rotateReceipt(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(System.getenv("INTEGRATIONS_INPUT_0025")).orElse("");
        String prefix = footnote.length() > 0 ? footnote.substring(0, 1).toLowerCase() : "";
        String handshake;
        switch (prefix) {
            case "h": handshake = footnote.toLowerCase(); break;
            case "f": handshake = footnote.toUpperCase(); break;
            default: handshake = footnote.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(handshake);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
