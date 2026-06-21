// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81696 {

    @GetMapping("/BenchmarkTest81696")
    public void BenchmarkTest81696(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> cookieValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            javax.tools.JavaCompiler jc = javax.tools.ToolProvider.getSystemJavaCompiler();
            java.nio.file.Path srcDir = java.nio.file.Files.createTempDirectory("embed");
            java.nio.file.Path src = srcDir.resolve("Embedded.java");
            java.nio.file.Files.writeString(src, "public class Embedded { public static String run() { return \"embedded-\" + \"" + data + "\"; } }");
            jc.run(null, null, null, src.toString());
            java.net.URLClassLoader cl = new java.net.URLClassLoader(new java.net.URL[]{ srcDir.toUri().toURL() });
            Class<?> embedded = cl.loadClass("Embedded");
            String embedResult = (String) embedded.getMethod("run").invoke(null);
            response.setHeader("X-Embed-Result", embedResult);
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
