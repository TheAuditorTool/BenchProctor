// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16558 {

    @GetMapping("/BenchmarkTest16558/{pathId}")
    public void BenchmarkTest16558(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "body");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        byte[] buf = new byte[Integer.parseInt(data)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
