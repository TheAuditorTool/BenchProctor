// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class BenchmarkTest54962 {

    @GET
    @Path("/BenchmarkTest54962")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest54962(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String prefix = hostValue.length() > 0 ? hostValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = hostValue.toLowerCase(); break;
            case "f": data = hostValue.toUpperCase(); break;
            default: data = hostValue.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(data);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
