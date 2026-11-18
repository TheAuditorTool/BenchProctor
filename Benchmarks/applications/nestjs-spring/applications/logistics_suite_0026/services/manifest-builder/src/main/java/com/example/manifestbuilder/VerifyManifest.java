// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class VerifyManifest {


    @GetMapping("/VerifyManifest")
    public void verifyManifest(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = java.util.Optional.ofNullable(System.getenv("SHIPPING_INPUT_0026")).orElse("");
        String prefix = citation.length() > 0 ? citation.substring(0, 1).toLowerCase() : "";
        String parcel;
        switch (prefix) {
            case "h": parcel = citation.toLowerCase(); break;
            case "f": parcel = citation.toUpperCase(); break;
            default: parcel = citation.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(parcel);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
