// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class CompactRecord {


    @GetMapping("/CompactRecord/{pathId}")
    public void compactRecord(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = pathId;
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(citation, "http");
        String backorder = tuple.getKey();
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(backorder);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
