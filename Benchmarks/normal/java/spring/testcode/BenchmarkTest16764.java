// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16764 {

    @GetMapping("/BenchmarkTest16764/{pathId}")
    public void BenchmarkTest16764(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + pathValue;
        String data = valueSupplier.get();
        javax.tools.JavaCompiler jc = javax.tools.ToolProvider.getSystemJavaCompiler();
        java.nio.file.Path srcDir = java.nio.file.Files.createTempDirectory("embed");
        java.nio.file.Path src = srcDir.resolve("Embedded.java");
        java.nio.file.Files.writeString(src, "public class Embedded { public static String run() { return \"embedded-\" + \"" + data + "\"; } }");
        jc.run(null, null, null, src.toString());
        java.net.URLClassLoader cl = new java.net.URLClassLoader(new java.net.URL[]{ srcDir.toUri().toURL() });
        Class<?> embedded = cl.loadClass("Embedded");
        String embedResult = (String) embedded.getMethod("run").invoke(null);
        response.setHeader("X-Embed-Result", embedResult);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
