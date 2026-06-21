// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest17552 {

    @GET
    @Path("/BenchmarkTest17552")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest17552(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.List<String> tokens = java.util.Arrays.asList(originValue.split(","));
        String data = String.join(",", tokens);
        javax.tools.JavaCompiler jc = javax.tools.ToolProvider.getSystemJavaCompiler();
        java.nio.file.Path srcDir = java.nio.file.Files.createTempDirectory("embed");
        java.nio.file.Path src = srcDir.resolve("Embedded.java");
        java.nio.file.Files.writeString(src, "public class Embedded { public static String run() { return \"embedded-\" + \"" + data + "\"; } }");
        jc.run(null, null, null, src.toString());
        java.net.URLClassLoader cl = new java.net.URLClassLoader(new java.net.URL[]{ srcDir.toUri().toURL() });
        Class<?> embedded = cl.loadClass("Embedded");
        String embedResult = (String) embedded.getMethod("run").invoke(null);
        response.setHeader("X-Embed-Result", embedResult);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
