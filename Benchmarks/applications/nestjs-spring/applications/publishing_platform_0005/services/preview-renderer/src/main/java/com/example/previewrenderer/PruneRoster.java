// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class PruneRoster {

    record FormData(String payload) {}

    @PostMapping(path="/PruneRoster", consumes="text/plain")
    public void pruneRoster(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        FormData payload = new FormData(footnote);
        String byline = payload.payload();
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(byline);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
