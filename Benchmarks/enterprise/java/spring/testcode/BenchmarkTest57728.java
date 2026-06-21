// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57728 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest57728")
    public void BenchmarkTest57728(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = expandTabs(hostValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
