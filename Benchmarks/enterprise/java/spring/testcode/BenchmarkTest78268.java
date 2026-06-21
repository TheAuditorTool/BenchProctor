// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78268 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest78268/{pathId}")
    public void BenchmarkTest78268(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
