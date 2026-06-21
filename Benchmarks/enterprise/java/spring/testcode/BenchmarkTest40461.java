// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest40461 {

    @GetMapping("/BenchmarkTest40461")
    public void BenchmarkTest40461(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        System.loadLibrary(hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
