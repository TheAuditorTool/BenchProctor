// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57075 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @PostMapping(path="/BenchmarkTest57075", consumes="multipart/form-data")
    public void BenchmarkTest57075(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        try { AllowedValue.valueOf(multipartValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { multipartValue = AllowedValue.values()[0].name().toLowerCase(); }
        new ProcessBuilder("python3", "-c", multipartValue).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
