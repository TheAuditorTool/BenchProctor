// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00791 {

    @POST
    @Path("/BenchmarkTest00791")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00791(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(rawData, "request");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        java.net.URL parsed = java.net.URI.create(data).toURL();
        java.util.Set<String> hosts = java.util.Set.of("api.svc.local", "cdn.acmecdn.net");
        if (!hosts.contains(parsed.getHost())) { return Response.status(403).build(); }
        String targetUrl = parsed.getProtocol() + "://" + parsed.getHost() + (parsed.getPort() == -1 ? "" : ":" + parsed.getPort());
        response.sendRedirect(targetUrl);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
