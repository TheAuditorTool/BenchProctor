// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67753 {

    @GetMapping("/BenchmarkTest67753")
    public void BenchmarkTest67753(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(uaValue, "json");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
