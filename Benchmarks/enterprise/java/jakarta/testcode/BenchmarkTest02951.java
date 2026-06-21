// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02951 {

    @GET
    @Path("/BenchmarkTest02951/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02951(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : pathValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        java.net.URL parsed = java.net.URI.create(data).toURL();
        java.util.Set<String> hosts = java.util.Set.of("api.svc.local", "cdn.acmecdn.net");
        if (!hosts.contains(parsed.getHost())) { return Response.status(403).build(); }
        String targetUrl = parsed.getProtocol() + "://" + parsed.getHost() + (parsed.getPort() == -1 ? "" : ":" + parsed.getPort());
        response.sendRedirect(targetUrl);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
