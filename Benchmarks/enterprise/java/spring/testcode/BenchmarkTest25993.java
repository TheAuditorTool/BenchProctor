// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25993 {

    @GetMapping("/BenchmarkTest25993")
    public void BenchmarkTest25993(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = "" + uaValue;
        int result = 100 / Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
