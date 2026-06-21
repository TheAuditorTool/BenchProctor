// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08890 {

    @GetMapping("/BenchmarkTest08890")
    public void BenchmarkTest08890(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(hostValue, "form");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
