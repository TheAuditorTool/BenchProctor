// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71805 {

    @PostMapping(path="/BenchmarkTest71805", consumes="application/xml")
    public void BenchmarkTest71805(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> xmlValue)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        if (!data.matches("^[\\w\\s<>\\\"'/().;=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
    }
}
