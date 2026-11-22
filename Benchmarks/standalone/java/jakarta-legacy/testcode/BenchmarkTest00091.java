// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00091 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @GET
    @Path("/BenchmarkTest00091/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00091(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = String.join(" ", pathValue.split("[ \\t]+"));
        String formulaSource = "public class Formula implements java.util.function.Supplier<Object> { public Object get() { return " + data + "; } }";
        javax.tools.JavaFileObject formulaUnit = new javax.tools.SimpleJavaFileObject(java.net.URI.create("string:///Formula.java"), javax.tools.JavaFileObject.Kind.SOURCE) { @Override public CharSequence getCharContent(boolean ignoreEncodingErrors) { return formulaSource; } };
        java.nio.file.Path formulaOut = java.nio.file.Files.createTempDirectory("formula");
        javax.tools.JavaCompiler formulaCompiler = javax.tools.ToolProvider.getSystemJavaCompiler();
        boolean formulaCompiled = formulaCompiler.getTask(null, null, null, java.util.List.of("-d", formulaOut.toString()), null, java.util.List.of(formulaUnit)).call();
        if (!formulaCompiled) { return Response.status(422).entity("formula did not compile").build(); }
        try (java.net.URLClassLoader formulaLoader = new java.net.URLClassLoader(new java.net.URL[]{ formulaOut.toUri().toURL() })) {
            Object formulaValue = ((java.util.function.Supplier<?>) formulaLoader.loadClass("Formula").getDeclaredConstructor().newInstance()).get();
            response.setHeader("X-Formula-Value", String.valueOf(formulaValue));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
