package com.example.hackathon2025.model;

public class User {

    private String id;
    private String name;
    private String university;
    private String course;
    private int year;

    // Matching-related fields
    private String interests;
    private String sleepSchedule;
    private int cleanliness;
    private int socialLevel;
    private String bio;

    // Constructors
    public User() { }

    public User(String id, String name, String university, String course, int year,
                String interests, String sleepSchedule, int cleanliness, int socialLevel, String bio) {
        this.id = id;
        this.name = name;
        this.university = university;
        this.course = course;
        this.year = year;
        this.interests = interests;
        this.sleepSchedule = sleepSchedule;
        this.cleanliness = cleanliness;
        this.socialLevel = socialLevel;
        this.bio = bio;
    }

    // Getters & Setters

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUniversity() {
        return university;
    }

    public void setUniversity(String university) {
        this.university = university;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getInterests() {
        return interests;
    }

    public void setInterests(String interests) {
        this.interests = interests;
    }

    public String getSleepSchedule() {
        return sleepSchedule;
    }

    public void setSleepSchedule(String sleepSchedule) {
        this.sleepSchedule = sleepSchedule;
    }

    public int getCleanliness() {
        return cleanliness;
    }

    public void setCleanliness(int cleanliness) {
        this.cleanliness = cleanliness;
    }

    public int getSocialLevel() {
        return socialLevel;
    }

    public void setSocialLevel(int socialLevel) {
        this.socialLevel = socialLevel;
    }

    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }
}
