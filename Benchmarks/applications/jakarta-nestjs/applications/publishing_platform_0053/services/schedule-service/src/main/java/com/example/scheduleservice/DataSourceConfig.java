package com.example.scheduleservice;

import javax.sql.DataSource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

@Configuration
public class DataSourceConfig {

    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource source = new DriverManagerDataSource();
        String dbUrl = System.getenv("DATABASE_URL");
        if (dbUrl != null && dbUrl.startsWith("postgres")) {
            java.net.URI dbUri = java.net.URI.create(dbUrl);
            String dbUserInfo = dbUri.getUserInfo() != null ? dbUri.getUserInfo() : "app:app";
            int dbSep = dbUserInfo.indexOf(':');
            source.setDriverClassName("org.postgresql.Driver");
            source.setUrl("jdbc:postgresql://" + dbUri.getHost() + ":" + (dbUri.getPort() == -1 ? 5432 : dbUri.getPort()) + dbUri.getPath() + "?" + (dbUri.getRawQuery() == null ? "" : dbUri.getRawQuery() + "&") + "stringtype=unspecified");
            source.setUsername(dbSep < 0 ? dbUserInfo : dbUserInfo.substring(0, dbSep));
            source.setPassword(dbSep < 0 ? "" : dbUserInfo.substring(dbSep + 1));
        } else {
            source.setDriverClassName("org.h2.Driver");
            source.setUrl("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1;NON_KEYWORDS=VALUE");
            source.setUsername("sa");
            source.setPassword("");
        }
        return source;
    }

    @Bean
    public JdbcTemplate jdbcTemplate(DataSource dataSource) {
        return new JdbcTemplate(dataSource);
    }
}
