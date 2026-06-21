// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51056 {

    @GetMapping("/BenchmarkTest51056")
    public void BenchmarkTest51056(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = "" + hostValue;
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
