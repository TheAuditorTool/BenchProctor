// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06209 {

    @GetMapping("/BenchmarkTest06209")
    public void BenchmarkTest06209(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(originValue, "json");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.sendError(500, data);
    }
}
