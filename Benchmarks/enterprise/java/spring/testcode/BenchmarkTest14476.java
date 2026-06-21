// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.yaml.snakeyaml.Yaml;

@RestController
public class BenchmarkTest14476 {

    @PostMapping(path="/BenchmarkTest14476", consumes="multipart/form-data")
    public void BenchmarkTest14476(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(multipartValue)); }
        catch (NumberFormatException e) { data = multipartValue; }
        Yaml yaml = new Yaml();
        Object obj = yaml.load(data);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
