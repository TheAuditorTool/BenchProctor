// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00753 {

    @GetMapping("/BenchmarkTest00753")
    public void BenchmarkTest00753(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(originValue, "json");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.getWriter().print("<div>" + data + "</div>");
    }
}
