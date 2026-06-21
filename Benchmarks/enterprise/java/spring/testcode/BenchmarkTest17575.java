// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17575 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest17575")
    public void BenchmarkTest17575(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
