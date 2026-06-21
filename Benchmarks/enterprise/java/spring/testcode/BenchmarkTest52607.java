// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52607 {

    @GetMapping("/BenchmarkTest52607/{pathId}")
    public void BenchmarkTest52607(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> firstStage = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(pathValue);
        java.net.URI parsed = java.net.URI.create(data);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.endsWith(".svc.local") && !parsedHost.endsWith(".acmecdn.net")) {
            response.sendError(403, "forbidden host"); return;
        }
        String targetUrl = data;
        response.setHeader("Access-Control-Allow-Origin", targetUrl);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
