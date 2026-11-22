package com.example.cyclecount;

@javax.persistence.Entity(name = "User")
@javax.persistence.Table(name = "users")
public class UserEntity {

    @javax.persistence.Id
    private Integer id;

    private String name;

    private String role;

    private String bio;

    private String email;

    public Integer getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getRole() {
        return role;
    }

    public String getBio() {
        return bio;
    }

    public String getEmail() {
        return email;
    }
}
