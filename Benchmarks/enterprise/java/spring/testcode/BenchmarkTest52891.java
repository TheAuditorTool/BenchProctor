// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52891 {

    @GetMapping("/BenchmarkTest52891")
    public void BenchmarkTest52891(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = hostValue.replace("\u0000", "");
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
