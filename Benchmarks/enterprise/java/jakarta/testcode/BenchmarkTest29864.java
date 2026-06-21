// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest29864 {

    @POST
    @Path("/BenchmarkTest29864")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest29864(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(xmlValue);
        byte[] buf = new byte[Integer.parseInt(data)];
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
