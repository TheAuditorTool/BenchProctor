// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08918 {

    @GetMapping("/BenchmarkTest08918")
    public void BenchmarkTest08918(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.format("payload=%s", hostValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
