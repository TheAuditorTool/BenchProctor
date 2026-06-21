// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01854 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @GET
    @Path("/BenchmarkTest01854")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01854(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        try { AllowedValue.valueOf(originValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { originValue = AllowedValue.values()[0].name().toLowerCase(); }
        String reflectStatus = "ok";
        try {
            Class<?> reflectCls = Class.forName(originValue);
            java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
            Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
            response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
        } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
        response.setHeader("X-Reflect-Status", reflectStatus);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
