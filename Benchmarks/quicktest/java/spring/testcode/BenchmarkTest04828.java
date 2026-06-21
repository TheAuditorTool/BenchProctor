// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04828 {

    @GetMapping("/BenchmarkTest04828")
    public void BenchmarkTest04828(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = hostValue.isEmpty() ? "default" : hostValue;
        new Socket(data, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
