// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79354 {

    @GetMapping("/BenchmarkTest79354")
    public void BenchmarkTest79354(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        response.setHeader("Access-Control-Allow-Origin", hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
