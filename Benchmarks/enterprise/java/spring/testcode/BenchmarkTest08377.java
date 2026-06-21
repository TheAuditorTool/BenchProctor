// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08377 {

    @GetMapping("/BenchmarkTest08377")
    public void BenchmarkTest08377(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(hostValue);
        String data = bundle.toString();
        response.sendError(500, data);
    }
}
