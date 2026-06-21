// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25316 {

    @GetMapping("/BenchmarkTest25316")
    public void BenchmarkTest25316(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        long seed = ((long) uaValue.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
