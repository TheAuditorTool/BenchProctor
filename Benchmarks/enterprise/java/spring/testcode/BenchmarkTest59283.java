// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59283 {

    @PostMapping(path="/BenchmarkTest59283", consumes="application/xml")
    public void BenchmarkTest59283(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(xmlValue);
        String data = normalizer.apply(xmlValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            try {
                java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(data)).GET().build();
                java.net.http.HttpResponse<String> fetchedResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
                javax.tools.JavaCompiler fetchJc = javax.tools.ToolProvider.getSystemJavaCompiler();
                java.nio.file.Path fetchDir = java.nio.file.Files.createTempDirectory("inc");
                java.nio.file.Path fetchSrc = fetchDir.resolve("Fetched.java");
                java.nio.file.Files.writeString(fetchSrc, fetchedResp.body());
                fetchJc.run(null, null, null, fetchSrc.toString());
                try (java.net.URLClassLoader fetchCl = new java.net.URLClassLoader(new java.net.URL[]{ fetchDir.toUri().toURL() })) {
                    Class<?> fetchedClass = fetchCl.loadClass("Fetched");
                    response.setHeader("X-Fetched-Class", fetchedClass.getName());
                }
            } catch (Exception e) { response.sendError(502); }
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
