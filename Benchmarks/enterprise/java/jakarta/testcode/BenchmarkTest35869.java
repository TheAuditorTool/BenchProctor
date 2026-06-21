// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest35869 {

    @POST
    @Path("/BenchmarkTest35869")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest35869(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::trim);
        String data = transformed.apply(xmlValue);
        return Response.status(500).entity(data).build();
    }
}
