// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76929 {

    @POST
    @Path("/BenchmarkTest76929")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76929(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        if (!fieldValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        javax.tools.JavaCompiler jc = javax.tools.ToolProvider.getSystemJavaCompiler();
        java.nio.file.Path srcDir = java.nio.file.Files.createTempDirectory("embed");
        java.nio.file.Path src = srcDir.resolve("Embedded.java");
        java.nio.file.Files.writeString(src, "public class Embedded { public static String run() { return \"embedded-\" + \"" + fieldValue + "\"; } }");
        jc.run(null, null, null, src.toString());
        java.net.URLClassLoader cl = new java.net.URLClassLoader(new java.net.URL[]{ srcDir.toUri().toURL() });
        Class<?> embedded = cl.loadClass("Embedded");
        String embedResult = (String) embedded.getMethod("run").invoke(null);
        response.setHeader("X-Embed-Result", embedResult);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
