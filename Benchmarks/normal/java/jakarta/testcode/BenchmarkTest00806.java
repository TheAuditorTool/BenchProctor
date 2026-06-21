// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00806 {

    @GET
    @Path("/BenchmarkTest00806")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00806(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + originValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        response.setHeader("X-Forwarded-For", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
