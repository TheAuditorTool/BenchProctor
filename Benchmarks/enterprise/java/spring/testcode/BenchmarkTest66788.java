// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66788 {

    @GetMapping("/BenchmarkTest66788")
    public void BenchmarkTest66788(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(envValue, "header");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
