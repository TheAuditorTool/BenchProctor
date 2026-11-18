// SPDX-License-Identifier: Apache-2.0
package com.example.customsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class EnrichBundle {


    @GetMapping("/EnrichBundle")
    public void enrichBundle(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(System.getenv("SHIPPING_INPUT_0035")).orElse("");
        String prefix = phrase.length() > 0 ? phrase.substring(0, 1).toLowerCase() : "";
        String parcel;
        switch (prefix) {
            case "h": parcel = phrase.toLowerCase(); break;
            case "f": parcel = phrase.toUpperCase(); break;
            default: parcel = phrase.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(parcel);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
