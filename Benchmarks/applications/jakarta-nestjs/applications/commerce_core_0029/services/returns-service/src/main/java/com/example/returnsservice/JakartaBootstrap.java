package com.example.returnsservice;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.returnsservice.JakartaBootstrap$HealthResource,com.example.returnsservice.ArchiveWindow,com.example.returnsservice.CollectFulfillment,com.example.returnsservice.EnrichProfile,com.example.returnsservice.FormatHeader,com.example.returnsservice.NormalizeCheckpoint,com.example.returnsservice.RequestReturn,com.example.returnsservice.RotateFulfillment,com.example.returnsservice.ValidateHeader");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
