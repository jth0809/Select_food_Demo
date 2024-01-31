package com.select_food.main.controller;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.select_food.main.model.RequestComponent;
import com.select_food.main.model.ResponseComponent;
import com.select_food.main.service.RequestService;

@CrossOrigin("*")
@RestController
public class MainController {
    private final RequestService requestService;

    @Autowired
    public MainController(RequestService requestService) {
        this.requestService = requestService;
    }

    @PostMapping("/api")
    public List<ResponseComponent> /*RequestComponent*/ api(@RequestBody RequestComponent requestComponent) {
        //System.out.println(requestComponent.getUserAllergy());
        //System.out.println(requestComponent.getUserReligion());
        //System.out.println(requestComponent.getLatitude());
        //System.out.println(requestComponent.getLongitude());
        //System.out.println(requestComponent.getUserVegan());
        //System.out.println(requestComponent.getUserDisease());
        return requestService.RequestOuter(requestComponent);
        //return requestComponent;
    }

}
