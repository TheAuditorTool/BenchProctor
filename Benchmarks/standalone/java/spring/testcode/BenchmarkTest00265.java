// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.yaml.snakeyaml.Yaml;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00265 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00265")
    public void BenchmarkTest00265(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(java.net.URI.create("https://api.svc.local/data").toURL().openStream())).readLine()).orElse("");
        String data = String.format("%s", apiBody);
        org.yaml.snakeyaml.LoaderOptions unsafeYamlOpts = new org.yaml.snakeyaml.LoaderOptions();
        unsafeYamlOpts.setTagInspector(tag -> true);
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.Constructor(unsafeYamlOpts));
        Object obj = yaml.load(data);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
