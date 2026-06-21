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
public class BenchmarkTest62796 {

    @GET
    @Path("/BenchmarkTest62796")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest62796(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + originValue;
        String data = valueSupplier.get();
        java.net.URL parsed = java.net.URI.create(data).toURL();
        java.util.Set<String> hosts = java.util.Set.of("api.svc.local", "cdn.acmecdn.net");
        if (!hosts.contains(parsed.getHost())) { return Response.status(403).build(); }
        String targetUrl = parsed.getProtocol() + "://" + parsed.getHost() + (parsed.getPort() == -1 ? "" : ":" + parsed.getPort());
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(targetUrl)).GET().build();
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
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
