// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33895 {

    @GetMapping("/BenchmarkTest33895")
    public void BenchmarkTest33895(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        Integer.parseInt(hostValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
