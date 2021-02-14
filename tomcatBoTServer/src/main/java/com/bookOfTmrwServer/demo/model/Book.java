package com.bookOfTmrwServer.demo.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonValue;

public class Book {
    private String name;

    public Book(@JsonProperty("name")String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }
}
