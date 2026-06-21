// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest46128 {

    @GetMapping("/BenchmarkTest46128")
    public void BenchmarkTest46128(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(refererValue);
        String data = envelope.toString();
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
