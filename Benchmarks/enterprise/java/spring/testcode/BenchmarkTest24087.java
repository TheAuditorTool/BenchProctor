// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.yaml.snakeyaml.Yaml;

@RestController
public class BenchmarkTest24087 {

    @GetMapping("/BenchmarkTest24087/{pathId}")
    public void BenchmarkTest24087(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(pathValue, "request");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        Yaml yaml = new Yaml();
        Object obj = yaml.load(data);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
