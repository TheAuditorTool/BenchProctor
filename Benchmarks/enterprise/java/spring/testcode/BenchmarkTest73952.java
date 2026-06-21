// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73952 {

    @GetMapping("/BenchmarkTest73952")
    public void BenchmarkTest73952(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        int result = 100 / Integer.parseInt(hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
