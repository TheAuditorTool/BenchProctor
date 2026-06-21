// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52398 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @PostMapping("/BenchmarkTest52398")
    public void BenchmarkTest52398(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        try { AllowedValue.valueOf(commentValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { commentValue = AllowedValue.values()[0].name().toLowerCase(); }
        String reflectStatus = "ok";
        try {
            Class<?> reflectCls = Class.forName(commentValue);
            java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
            Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
            response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
        } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
        response.setHeader("X-Reflect-Status", reflectStatus);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
