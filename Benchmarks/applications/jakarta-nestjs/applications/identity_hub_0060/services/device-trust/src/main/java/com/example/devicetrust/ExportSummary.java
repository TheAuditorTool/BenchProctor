// SPDX-License-Identifier: Apache-2.0
package com.example.devicetrust;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class ExportSummary {


    @GET
    @Path("/ExportSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportSummary(@jakarta.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = sessionToken != null ? sessionToken : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(paragraph, "header");
        String persona = pair.getKey();
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(persona);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
