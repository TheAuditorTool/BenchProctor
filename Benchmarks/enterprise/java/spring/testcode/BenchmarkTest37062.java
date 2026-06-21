// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37062 {

    @GetMapping("/BenchmarkTest37062")
    public void BenchmarkTest37062(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        response.setContentType("text/html");
        response.getWriter().print(hostValue);
    }
}
