// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00247 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00247")
    public void BenchmarkTest00247(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", uaValue);
        String data = sw.toString();
        String formulaSource = "public class Formula implements java.util.function.Supplier<Object> { public Object get() { return " + data + "; } }";
        javax.tools.JavaFileObject formulaUnit = new javax.tools.SimpleJavaFileObject(java.net.URI.create("string:///Formula.java"), javax.tools.JavaFileObject.Kind.SOURCE) { @Override public CharSequence getCharContent(boolean ignoreEncodingErrors) { return formulaSource; } };
        java.nio.file.Path formulaOut = java.nio.file.Files.createTempDirectory("formula");
        javax.tools.JavaCompiler formulaCompiler = javax.tools.ToolProvider.getSystemJavaCompiler();
        boolean formulaCompiled = formulaCompiler.getTask(null, null, null, java.util.List.of("-d", formulaOut.toString()), null, java.util.List.of(formulaUnit)).call();
        if (!formulaCompiled) { response.sendError(422, "formula did not compile"); return; }
        try (java.net.URLClassLoader formulaLoader = new java.net.URLClassLoader(new java.net.URL[]{ formulaOut.toUri().toURL() })) {
            Object formulaValue = ((java.util.function.Supplier<?>) formulaLoader.loadClass("Formula").getDeclaredConstructor().newInstance()).get();
            response.setHeader("X-Formula-Value", String.valueOf(formulaValue));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
