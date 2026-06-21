// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17898 {

    @GetMapping("/BenchmarkTest17898")
    public void BenchmarkTest17898(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(refererValue, "form");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
