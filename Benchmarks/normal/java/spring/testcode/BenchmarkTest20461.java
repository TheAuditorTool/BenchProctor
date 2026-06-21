// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest20461 {

    @PostMapping(path="/BenchmarkTest20461", consumes="multipart/form-data")
    public void BenchmarkTest20461(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        StringBuilder payload = new StringBuilder();
        payload.append(uploadName);
        String data = payload.toString();
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
