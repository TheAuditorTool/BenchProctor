// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest03172 {

    @GET
    @Path("/BenchmarkTest03172")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03172(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(secretValue);
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
