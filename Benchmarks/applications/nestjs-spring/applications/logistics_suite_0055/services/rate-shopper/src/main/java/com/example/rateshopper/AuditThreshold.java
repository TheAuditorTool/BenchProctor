// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class AuditThreshold {


    @PostMapping(path="/AuditThreshold", consumes="text/plain")
    public void auditThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = rawBody != null ? rawBody : "";
        byte[] raw = heading.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String consignment = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        org.yaml.snakeyaml.LoaderOptions unsafeYamlOpts = new org.yaml.snakeyaml.LoaderOptions();
        unsafeYamlOpts.setTagInspector(tag -> true);
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.Constructor(unsafeYamlOpts));
        Object obj = yaml.load(consignment);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
