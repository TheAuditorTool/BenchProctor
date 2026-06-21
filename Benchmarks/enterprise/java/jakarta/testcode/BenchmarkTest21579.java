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
public class BenchmarkTest21579 {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest21579")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21579(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        sharedRef.set(originValue);
        String data = sharedRef.get();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
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
            } catch (Exception e) { response.sendError(502); }
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
