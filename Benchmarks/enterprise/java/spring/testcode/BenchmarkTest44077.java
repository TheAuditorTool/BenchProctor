// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44077 {

    @GetMapping("/BenchmarkTest44077")
    public void BenchmarkTest44077(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = "" + hostValue;
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
