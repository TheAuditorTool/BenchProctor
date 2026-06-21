// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest03698 {

    @GET
    @Path("/BenchmarkTest03698")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03698(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{headerValue});
        java.net.URI parsedUri = java.net.URI.create(data.contains("://") ? data : "https://" + data);
        java.net.InetAddress addr = java.net.InetAddress.getByName(parsedUri.getHost());
        if (addr.isAnyLocalAddress() || addr.isLoopbackAddress() || addr.isSiteLocalAddress() || addr.isLinkLocalAddress()) {
            return Response.status(403).build();
        }
        String targetUrl = parsedUri.getScheme() + "://" + parsedUri.getHost() + (parsedUri.getPort() == -1 ? "" : ":" + parsedUri.getPort());
        new Socket(targetUrl, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
