// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77781 {

    @PostMapping(path="/BenchmarkTest77781", consumes="application/xml")
    public void BenchmarkTest77781(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data;
        if (xmlValue.length() > 256) { data = xmlValue.substring(0, 256); }
        else { data = xmlValue; }
        String reflectStatus = "ok";
        try {
            Class<?> reflectCls = Class.forName(data);
            java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
            Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
            response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
        } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
        response.setHeader("X-Reflect-Status", reflectStatus);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
