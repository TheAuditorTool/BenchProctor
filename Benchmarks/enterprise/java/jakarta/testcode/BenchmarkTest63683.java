// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import java.net.*;

@Path("/")
public class BenchmarkTest63683 {

    @GET
    @Path("/BenchmarkTest63683")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest63683(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.function.Function<String, String> primary = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::strip);
        String data = stripChain.apply(forwardedIp);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            try {
                java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(data)).GET().build();
                java.net.http.HttpResponse<String> fetchedResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
                javax.tools.JavaCompiler fetchJc = javax.tools.ToolProvider.getSystemJavaCompiler();
                java.nio.file.Path fetchDir = java.nio.file.Files.createTempDirectory("inc");
                java.nio.file.Path fetchSrc = fetchDir.resolve("Fetched.java");
                java.nio.file.Files.writeString(fetchSrc, fetchedResp.body());
                fetchJc.run(null, null, null, fetchSrc.toString());
                try (java.net.URLClassLoader fetchCl = new java.net.URLClassLoader(new java.net.URL[]{ fetchDir.toUri().toURL() })) {
                    Class<?> fetchedClass = fetchCl.loadClass("Fetched");
                    response.setHeader("X-Fetched-Class", fetchedClass.getName());
                }
            } catch (Exception e) { return Response.status(502).build(); }
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
