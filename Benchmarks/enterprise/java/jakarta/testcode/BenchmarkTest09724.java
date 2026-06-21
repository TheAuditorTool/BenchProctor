// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09724 {

    @GET
    @Path("/BenchmarkTest09724")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09724(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(hostValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.getSession().setAttribute("data", String.valueOf(processed));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
