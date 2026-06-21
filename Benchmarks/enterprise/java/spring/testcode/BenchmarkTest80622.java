// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest80622 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest80622.class);
    private static final class ValidatedDto {
        @jakarta.validation.constraints.NotNull
        @jakarta.validation.constraints.Pattern(regexp = "^[A-Za-z0-9_.-]+$")
        @jakarta.validation.constraints.Size(max = 256)
        public String value;
        ValidatedDto(String v) { this.value = v; }
    }
    private static final jakarta.validation.Validator VALIDATOR =
        jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();

    @PostMapping(path="/BenchmarkTest80622", consumes="multipart/form-data")
    public void BenchmarkTest80622(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = "" + uploadName;
        java.util.Set<jakarta.validation.ConstraintViolation<ValidatedDto>> violations = VALIDATOR.validate(new ValidatedDto(data));
        if (!violations.isEmpty()) { response.sendError(400, "schema invalid"); return; }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
