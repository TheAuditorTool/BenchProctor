// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07489 {

    @GET
    @Path("/BenchmarkTest07489/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07489(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Properties property = new java.util.Properties();
        property.load(new java.io.StringReader("rawValue=" + pathValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", property.getProperty("format", "plain"));
        String data = property.getProperty("rawValue", "");
        if (request.getUserPrincipal() == null) {
            return Response.status(401).entity("not authenticated").build();
        }
        String oldSessionId = request.getSession().getId();
        request.getSession().invalidate();
        request.getSession(true).setAttribute("rotated_from", oldSessionId);
        if (request.getSession().getAttribute("user") == null) { return Response.status(401).build(); }
        request.getSession().setAttribute("data", String.valueOf(data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
