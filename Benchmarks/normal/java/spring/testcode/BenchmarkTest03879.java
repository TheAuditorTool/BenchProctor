// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03879 {

    @GetMapping("/BenchmarkTest03879")
    public void BenchmarkTest03879(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        if (!hostValue.isEmpty()) throw new IllegalArgumentException("invalid input: " + hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
