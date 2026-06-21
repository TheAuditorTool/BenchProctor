// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47162 {

    @PostMapping(path="/BenchmarkTest47162", consumes="application/xml")
    public void BenchmarkTest47162(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String prefix = xmlValue.length() > 0 ? xmlValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = xmlValue.toLowerCase(); break;
            case "f": data = xmlValue.toUpperCase(); break;
            default: data = xmlValue.strip(); break;
        }
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
