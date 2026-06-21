// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12975 {

    @GetMapping("/BenchmarkTest12975")
    public void BenchmarkTest12975(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = hostValue.isEmpty() ? "default" : hostValue;
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
