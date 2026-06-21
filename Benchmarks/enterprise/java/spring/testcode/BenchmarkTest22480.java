// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22480 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest22480/{pathId}")
    public void BenchmarkTest22480(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = trimEnds(pathValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
