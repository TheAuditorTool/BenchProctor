// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import java.net.*;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00248 {

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
    @Path("/BenchmarkTest00248")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00248(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", hostValue);
        String data = sw.toString();
        java.net.URI parsedUri = java.net.URI.create(data.contains("://") ? data : "https://" + data);
        String resolvedIp = java.net.InetAddress.getByName(parsedUri.getHost()).getHostAddress();
        if (java.util.regex.Pattern.compile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").matcher(resolvedIp).find()) { return Response.status(403).build(); }
        String targetUrl = data;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(targetUrl)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
