// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20246 {

    @GET
    @Path("/BenchmarkTest20246")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20246(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + userId.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
