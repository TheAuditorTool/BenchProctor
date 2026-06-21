// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02659 {

    @GET
    @Path("/BenchmarkTest02659")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02659(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> normalized = initialFn.andThen(String::strip);
        String data = normalized.apply(hostValue);
        return Response.status(500).entity(data).build();
    }
}
