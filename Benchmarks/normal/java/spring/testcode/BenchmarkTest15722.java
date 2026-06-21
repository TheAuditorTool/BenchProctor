// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15722 {

    @GetMapping("/BenchmarkTest15722")
    public void BenchmarkTest15722(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : cookieValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
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
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
