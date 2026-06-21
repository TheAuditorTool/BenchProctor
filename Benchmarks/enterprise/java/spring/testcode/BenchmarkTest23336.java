// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23336 {

    @GetMapping("/BenchmarkTest23336")
    public void BenchmarkTest23336(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(originValue, "http");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        if ("admin".equals(data)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
