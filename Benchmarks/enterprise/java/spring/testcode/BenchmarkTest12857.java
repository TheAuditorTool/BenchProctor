// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12857 {

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(64))");
                stmt.execute("INSERT INTO users (id, name) VALUES (1, 'alice')");
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static String dbReadColumn(String sql) {
        try (var stmt = connection.createStatement();
             var rs = stmt.executeQuery(sql)) {
            return rs.next() ? rs.getString(1) : "";
        } catch (java.sql.SQLException e) {
            return "";
        }
    }
    private static final class ValidatedDto {
        @jakarta.validation.constraints.NotNull
        @jakarta.validation.constraints.Pattern(regexp = "^[A-Za-z0-9_.-]+$")
        @jakarta.validation.constraints.Size(max = 256)
        public String value;
        ValidatedDto(String v) { this.value = v; }
    }
    private static final jakarta.validation.Validator VALIDATOR =
        jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();

    @GetMapping("/BenchmarkTest12857")
    public void BenchmarkTest12857(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userName = java.util.Optional.ofNullable(dbReadColumn("SELECT name FROM users LIMIT 1")).orElse("");
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userName)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        java.util.Set<jakarta.validation.ConstraintViolation<ValidatedDto>> violations = VALIDATOR.validate(new ValidatedDto(data));
        if (!violations.isEmpty()) { response.sendError(400, "schema invalid"); return; }
        Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
