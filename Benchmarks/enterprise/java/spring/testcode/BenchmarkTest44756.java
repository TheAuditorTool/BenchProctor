// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44756 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping(path="/BenchmarkTest44756", consumes="multipart/form-data")
    public void BenchmarkTest44756(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = expandTabs(multipartValue);
        java.net.URI parsed = java.net.URI.create(data);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.endsWith(".svc.local") && !parsedHost.endsWith(".acmecdn.net")) {
            response.sendError(403, "forbidden host"); return;
        }
        String targetUrl = data;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(targetUrl)).GET().build();
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
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
