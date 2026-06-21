// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81064 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest81064")
    public void BenchmarkTest81064(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = trimEnds(originValue);
        response.sendError(500, data);
    }
}
