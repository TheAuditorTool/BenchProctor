// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70514 {

    private enum AllowedValue { APPLICATION_JSON, TEXT_PLAIN, TEXT_HTML, APPLICATION_XML }

    @PostMapping(path="/BenchmarkTest70514", consumes="multipart/form-data")
    public void BenchmarkTest70514(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + multipartValue;
        String data = valueSupplier.get();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        response.setHeader("X-Forwarded-For", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
