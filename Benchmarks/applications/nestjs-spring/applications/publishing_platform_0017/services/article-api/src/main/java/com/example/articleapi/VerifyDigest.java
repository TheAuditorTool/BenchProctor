// SPDX-License-Identifier: Apache-2.0
package com.example.articleapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class VerifyDigest {


    @PostMapping(path="/VerifyDigest", consumes="text/plain")
    public void verifyDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = rawBody != null ? rawBody : "";
        byte[] raw = summary.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String addendum = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        org.yaml.snakeyaml.LoaderOptions unsafeYamlOpts = new org.yaml.snakeyaml.LoaderOptions();
        unsafeYamlOpts.setTagInspector(tag -> true);
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.Constructor(unsafeYamlOpts));
        Object obj = yaml.load(addendum);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
