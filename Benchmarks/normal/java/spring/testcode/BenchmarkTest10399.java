// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10399 {

    @GetMapping("/BenchmarkTest10399")
    public void BenchmarkTest10399(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : hostValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
