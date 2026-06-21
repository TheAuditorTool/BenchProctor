// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class BenchmarkTest11260 {

    @GET
    @Path("/BenchmarkTest11260")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11260(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        String prefix = apiBody.length() > 0 ? apiBody.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = apiBody.toLowerCase(); break;
            case "f": data = apiBody.toUpperCase(); break;
            default: data = apiBody.strip(); break;
        }
        Yaml yaml = new Yaml();
        Object obj = yaml.load(data);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
