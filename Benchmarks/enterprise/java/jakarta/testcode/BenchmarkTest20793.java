// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20793 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @GET
    @Path("/BenchmarkTest20793/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20793(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = pathValue.isEmpty() ? "default" : pathValue;
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        String reflectStatus = "ok";
        try {
            Class<?> reflectCls = Class.forName(data);
            java.lang.reflect.Method reflectMethod = reflectCls.getDeclaredMethod("toString");
            Object invokeResult = reflectMethod.invoke(reflectCls.getDeclaredConstructor().newInstance());
            response.setHeader("X-Reflect-Result", String.valueOf(invokeResult));
        } catch (ReflectiveOperationException re) { reflectStatus = "class-not-found"; }
        response.setHeader("X-Reflect-Status", reflectStatus);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
