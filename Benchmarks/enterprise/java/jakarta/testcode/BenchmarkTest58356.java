// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest58356 {

    @GET
    @Path("/BenchmarkTest58356/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest58356(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + pathValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
