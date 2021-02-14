package com.bookOfTmrwServer.demo.controller;


import com.bookOfTmrwServer.demo.model.Book;
import com.bookOfTmrwServer.demo.model.User;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.PostConstruct;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;

@RestController
public class controller {
    private ArrayList<User> userArrayList;

    @PostConstruct
    public void initIt(){
        try{
            ObjectMapper mapper = new ObjectMapper();
            userArrayList = new ArrayList<>(Arrays.asList(
                    mapper.readValue(
                            Paths.get("src/main/resources/data/userBookList.json").toFile(),
                            User[].class)));
            System.out.println("Book: "+ userArrayList.get(0).getBook(0).getName());
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    @GetMapping("/api/userList/{id}")
    public ArrayList<Book> getBookList (@PathVariable String id, HttpServletResponse response) throws IOException{
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                System.out.println("getBookList called, returning userArrayList.get(id)");
                response.setStatus(200);
                return userArrayList.get(i).getBookArrayList();
            }
        }
        System.out.println("Invalid ID, returning null");

        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
        response.sendError(HttpServletResponse.SC_NOT_FOUND, "ID invalid");
        return null;
    }
}
