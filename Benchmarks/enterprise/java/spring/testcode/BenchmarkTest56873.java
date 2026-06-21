// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56873 {

    @GetMapping("/BenchmarkTest56873/{pathId}")
    public void BenchmarkTest56873(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> primary = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::trim);
        String data = stripChain.apply(pathValue);
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
