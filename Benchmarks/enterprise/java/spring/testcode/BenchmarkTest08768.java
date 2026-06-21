// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08768 {

    @GetMapping("/BenchmarkTest08768")
    public void BenchmarkTest08768(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(authHeader, "http");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.sendError(500, data);
    }
}
