// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class PruneShipment {


    @GetMapping("/PruneShipment/{pathId}")
    public void pruneShipment(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(caption, "request");
        String parcel = kv.getKey();
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(parcel);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
