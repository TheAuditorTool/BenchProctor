// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00703 {

    @GetMapping("/BenchmarkTest00703")
    public void BenchmarkTest00703(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = hostValue.isEmpty() ? "default" : hostValue;
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
