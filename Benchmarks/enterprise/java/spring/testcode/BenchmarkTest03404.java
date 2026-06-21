// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest03404 {

    @PostMapping(path="/BenchmarkTest03404", consumes="multipart/form-data")
    public void BenchmarkTest03404(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(uploadName);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
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
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
