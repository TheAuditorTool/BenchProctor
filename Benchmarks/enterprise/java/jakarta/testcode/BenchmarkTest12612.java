// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12612 {

    @GET
    @Path("/BenchmarkTest12612")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12612(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder bundle = new StringBuilder();
        bundle.append(envValue);
        String data = bundle.toString();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            javax.tools.JavaCompiler jc = javax.tools.ToolProvider.getSystemJavaCompiler();
            java.nio.file.Path srcDir = java.nio.file.Files.createTempDirectory("embed");
            java.nio.file.Path src = srcDir.resolve("Embedded.java");
            java.nio.file.Files.writeString(src, "public class Embedded { public static String run() { return \"embedded-\" + \"" + data + "\"; } }");
            jc.run(null, null, null, src.toString());
            java.net.URLClassLoader cl = new java.net.URLClassLoader(new java.net.URL[]{ srcDir.toUri().toURL() });
            Class<?> embedded = cl.loadClass("Embedded");
            String embedResult = (String) embedded.getMethod("run").invoke(null);
            response.setHeader("X-Embed-Result", embedResult);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
