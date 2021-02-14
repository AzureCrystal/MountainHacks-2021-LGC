package com.bookOfTmrwServer.demo.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonValue;

import java.util.ArrayList;

public class User {
    private String id;
    private ArrayList<Book> bookArrayList;

    public User(@JsonProperty("id")String id, @JsonProperty("books")ArrayList<Book>bookArrayList){
        this.id = id;
        this.bookArrayList = bookArrayList;
    }

    public Book getBook(int index){
        return bookArrayList.get(index);
    }

    public ArrayList<Book> getBookArrayList(){
        return this.bookArrayList;
    }

    public String getId(){
        return this.id;
    }

}
