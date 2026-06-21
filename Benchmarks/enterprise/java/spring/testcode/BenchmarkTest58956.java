// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58956 {

    @GetMapping("/BenchmarkTest58956")
    public void BenchmarkTest58956(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder payload = new StringBuilder();
        payload.append(uaValue);
        String data = payload.toString();
        byte[] buf = new byte[Integer.parseInt(data)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
