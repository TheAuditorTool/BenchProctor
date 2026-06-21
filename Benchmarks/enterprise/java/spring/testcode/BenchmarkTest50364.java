// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50364 {

    @GetMapping("/BenchmarkTest50364")
    public void BenchmarkTest50364(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(uaValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            String reflectStatus = "ok";
            try {
                Class<?> reflectCls = Class.forName(data);
                java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
                Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
                response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
            } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
            response.setHeader("X-Reflect-Status", reflectStatus);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
