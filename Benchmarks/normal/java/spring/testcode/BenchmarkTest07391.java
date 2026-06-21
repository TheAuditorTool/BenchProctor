// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest07391 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @PostMapping(path="/BenchmarkTest07391", consumes="multipart/form-data")
    public void BenchmarkTest07391(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        try { AllowedValue.valueOf(uploadName.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { uploadName = AllowedValue.values()[0].name().toLowerCase(); }
        Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(uploadName).getValue();
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
