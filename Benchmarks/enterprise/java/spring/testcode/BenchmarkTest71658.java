// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71658 {

    @PostMapping(path="/BenchmarkTest71658", consumes="text/plain")
    public void BenchmarkTest71658(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(rawData, "form");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
