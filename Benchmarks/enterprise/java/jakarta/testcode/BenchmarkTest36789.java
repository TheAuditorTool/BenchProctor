// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest36789 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GET
    @Path("/BenchmarkTest36789")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest36789(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        FormData payload = new FormData(authHeader);
        String data = payload.payload;
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
