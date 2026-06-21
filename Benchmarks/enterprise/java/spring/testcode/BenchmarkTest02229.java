// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.yaml.snakeyaml.Yaml;

@RestController
public class BenchmarkTest02229 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest02229/{pathId}")
    public void BenchmarkTest02229(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        Yaml yaml = new Yaml();
        Object obj = yaml.load(data);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
