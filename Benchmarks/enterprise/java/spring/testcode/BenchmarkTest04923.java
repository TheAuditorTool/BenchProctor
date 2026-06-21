// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04923 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest04923")
    public void BenchmarkTest04923(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
