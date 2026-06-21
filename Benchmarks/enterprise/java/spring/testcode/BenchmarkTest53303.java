// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53303 {

    @GetMapping("/BenchmarkTest53303")
    public void BenchmarkTest53303(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data;
        if (uaValue.length() > 256) { data = uaValue.substring(0, 256); }
        else { data = uaValue; }
        response.sendError(500, data);
    }
}
