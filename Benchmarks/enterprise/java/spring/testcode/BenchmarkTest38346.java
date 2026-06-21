// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38346 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GetMapping("/BenchmarkTest38346")
    public void BenchmarkTest38346(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = toLowerCase(userId);
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
