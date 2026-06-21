// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01113 {

    @GetMapping("/BenchmarkTest01113/{pathId}")
    public void BenchmarkTest01113(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "json");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
