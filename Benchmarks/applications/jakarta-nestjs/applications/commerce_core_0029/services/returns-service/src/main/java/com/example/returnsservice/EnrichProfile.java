// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class EnrichProfile {


    @GET
    @Path("/EnrichProfile")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichProfile(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = origin != null ? origin : "";
        String backorder;
        if (notice.length() > 256) { backorder = notice.substring(0, 256); }
        else { backorder = notice; }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(backorder);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
