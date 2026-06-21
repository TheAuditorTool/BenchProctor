// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest31593 {

    @GET
    @Path("/BenchmarkTest31593")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest31593(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(hostValue, "json");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        byte[] buf = new byte[Integer.parseInt(data)];
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
