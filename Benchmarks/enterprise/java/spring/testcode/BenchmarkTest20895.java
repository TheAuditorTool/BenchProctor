// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20895 {

    @GetMapping("/BenchmarkTest20895")
    public void BenchmarkTest20895(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + hostValue + "\"}");
    }
}
