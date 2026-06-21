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
public class BenchmarkTest46026 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GET
    @Path("/BenchmarkTest46026")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest46026(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = toLowerCase(refererValue);
        java.net.URI parsed = java.net.URI.create(data);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.endsWith(".svc.local") && !parsedHost.endsWith(".acmecdn.net")) {
            return Response.status(403).entity("forbidden host").build();
        }
        String targetUrl = data;
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
