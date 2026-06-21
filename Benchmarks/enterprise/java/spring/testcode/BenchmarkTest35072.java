// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35072 {

    @GetMapping("/BenchmarkTest35072")
    public void BenchmarkTest35072(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = "[%s]".formatted(hostValue);
        response.sendError(500, data);
    }
}
