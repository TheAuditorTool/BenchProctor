// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class IndexMetadata {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("media_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/IndexMetadata")
    public void indexMetadata(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = inboundPayload.value != null ? inboundPayload.value : "";
        org.yaml.snakeyaml.LoaderOptions unsafeYamlOpts = new org.yaml.snakeyaml.LoaderOptions();
        unsafeYamlOpts.setTagInspector(tag -> true);
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.Constructor(unsafeYamlOpts));
        Object obj = yaml.load(paragraph);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
