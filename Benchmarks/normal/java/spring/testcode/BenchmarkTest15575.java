// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.util.Random;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15575 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest15575/{pathId}")
    public void BenchmarkTest15575(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = stripCRLF(pathValue);
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
