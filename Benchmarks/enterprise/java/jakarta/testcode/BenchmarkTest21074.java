// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21074 {

    @GET
    @Path("/BenchmarkTest21074/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21074(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Properties property = new java.util.Properties();
        property.load(new java.io.StringReader("rawValue=" + pathValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", property.getProperty("format", "plain"));
        String data = property.getProperty("rawValue", "");
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
