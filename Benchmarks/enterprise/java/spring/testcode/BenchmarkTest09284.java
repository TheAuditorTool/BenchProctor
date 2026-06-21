// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09284 {

    @GetMapping("/BenchmarkTest09284")
    public void BenchmarkTest09284(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> envValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            javax.tools.JavaCompiler jc = javax.tools.ToolProvider.getSystemJavaCompiler();
            java.nio.file.Path srcDir = java.nio.file.Files.createTempDirectory("embed");
            java.nio.file.Path src = srcDir.resolve("Embedded.java");
            java.nio.file.Files.writeString(src, "public class Embedded { public static String run() { return \"embedded-\" + \"" + data + "\"; } }");
            jc.run(null, null, null, src.toString());
            java.net.URLClassLoader cl = new java.net.URLClassLoader(new java.net.URL[]{ srcDir.toUri().toURL() });
            Class<?> embedded = cl.loadClass("Embedded");
            String embedResult = (String) embedded.getMethod("run").invoke(null);
            response.setHeader("X-Embed-Result", embedResult);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
