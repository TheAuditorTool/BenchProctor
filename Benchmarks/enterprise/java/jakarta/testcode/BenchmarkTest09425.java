// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest09425 {

    @GET
    @Path("/BenchmarkTest09425")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09425(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        String data = String.join(" ", apiBody.split("\\s+"));
        new Socket(data, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
