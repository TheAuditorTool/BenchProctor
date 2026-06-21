// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73489 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest73489")
    public void BenchmarkTest73489(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        valueRef.set(hostValue);
        String data = valueRef.get();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            try {
                java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(data)).GET().build();
                java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
                response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
            } catch (Exception e) { response.sendError(502); }
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
