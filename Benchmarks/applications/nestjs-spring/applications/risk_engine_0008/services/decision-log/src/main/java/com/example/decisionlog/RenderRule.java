// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class RenderRule {


    @PostMapping(path="/RenderRule", consumes="text/plain")
    public void renderRule(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = rawBody != null ? rawBody : "";
        byte[] raw = synopsis.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String verdict = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        org.yaml.snakeyaml.LoaderOptions unsafeYamlOpts = new org.yaml.snakeyaml.LoaderOptions();
        unsafeYamlOpts.setTagInspector(tag -> true);
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.Constructor(unsafeYamlOpts));
        Object obj = yaml.load(verdict);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
