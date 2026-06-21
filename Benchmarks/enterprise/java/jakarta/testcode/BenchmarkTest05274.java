// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest05274 {

    @GET
    @Path("/BenchmarkTest05274")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05274(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        String data;
        if (secretValue.length() > 256) { data = secretValue.substring(0, 256); }
        else { data = secretValue; }
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
