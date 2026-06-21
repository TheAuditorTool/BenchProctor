// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47453 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest47453")
    public void BenchmarkTest47453(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = stripCRLF(hostValue);
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
