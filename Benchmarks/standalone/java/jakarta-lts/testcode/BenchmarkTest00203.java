// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00203 {

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

    @POST
    @Path("/BenchmarkTest00203")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00203(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Supplier<String> valueSupplier = () -> xmlValue.strip();
        String data = valueSupplier.get();
        String processed = data.matches("^(noop|identity|passthrough|echo)$") ? data : "noop";
        String formulaSource = "public class Formula implements java.util.function.Supplier<Object> { public Object get() { return " + processed + "; } }";
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
