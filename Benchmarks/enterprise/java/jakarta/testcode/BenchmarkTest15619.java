// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest15619 {

    @POST
    @Path("/BenchmarkTest15619")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest15619(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.net.URI parsedUri = java.net.URI.create(xmlValue.contains("://") ? xmlValue : "https://" + xmlValue);
        java.net.InetAddress addr = java.net.InetAddress.getByName(parsedUri.getHost());
        if (addr.isAnyLocalAddress() || addr.isLoopbackAddress() || addr.isSiteLocalAddress() || addr.isLinkLocalAddress()) {
            return Response.status(403).build();
        }
        String targetUrl = parsedUri.getScheme() + "://" + parsedUri.getHost() + (parsedUri.getPort() == -1 ? "" : ":" + parsedUri.getPort());
        new Socket(targetUrl, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
