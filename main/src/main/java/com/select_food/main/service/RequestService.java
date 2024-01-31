package com.select_food.main.service;


//import org.apache.catalina.connector.Request;
//import org.apache.catalina.connector.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.client.RestTemplate;

//import com.select_food.main.model.Locationinfo;
import com.select_food.main.model.RequestComponent;
import com.select_food.main.model.ResponseComponent;
import com.select_food.main.model.sampleinfo;
import com.select_food.main.repository.LocationRepo;
import com.select_food.main.repository.MenuRepo;
import com.select_food.main.repository.SampleRepo;
import com.select_food.main.repository.TagRepo;

import java.util.ArrayList;
import java.util.List;
import lombok.Getter;
import lombok.NoArgsConstructor;
//import lombok.RequiredArgsConstructor;
import lombok.Setter;

@CrossOrigin("*")
@EnableJpaRepositories(basePackages = "com.select_food.main.repository")
@NoArgsConstructor
@Getter
@Service
public class RequestService {

    @Autowired
    private LocationRepo locat;
    private MenuRepo menu;
    private SampleRepo sample;
    private TagRepo tag;

    @Autowired
    public RequestService(LocationRepo locat,MenuRepo menu,SampleRepo sample,TagRepo tag) {
        this.locat = locat;
        this.menu = menu;
        this.sample = sample;
        this.tag = tag;
    }

    public class location {
        public Double latitude;
        public Double longitude;
    }
    @Getter
    @Setter
    public static class food {
        private String Menus = "문어순대국";
    }
    @Getter
    @Setter
    static class ai {
        private String food_name;
    }
    //위치정보를 받아서 음식점 정보를 받아오는 api를 호출하는 부분
    //사용자에게 받아온 위치정보를 이용해서 주변 위치정보를 계산하고 셀레니움을 호출해 음식점명을 받아와서 API 호출 혹은 DB를 통해서 메뉴를 받아옴
    public List<ResponseComponent> RequestOuter(RequestComponent requestComponent) {
        /*RestTemplate restTemplate = new RestTemplate();
        String url = "";        
        requestComponent = new RequestComponent(0,1,2,3);

        location loca = new location();
        loca.latitude = requestComponent.getLatitude();
        loca.longitude = requestComponent.getLongitude();
        Locationinfo locationinfo = new Locationinfo();
        
        HttpHeaders headers = new HttpHeaders();

        List<Locationinfo> locations = this.locat.findByLatitudeAndLongitude(loca.latitude, loca.longitude);
        */

    //DEMO
        List<sampleinfo> samples = this.sample.findAll();
        List<ResponseComponent> menus = new ArrayList<ResponseComponent>();

        List<Integer> list1 = new ArrayList<>(List.of(4,4,4,4));//(List.of(requestComponent.getUserDisease(),requestComponent.getUserAllergy(),requestComponent.getUserReligion(),requestComponent.getUserVegan()?1:0));
        if(requestComponent.getUserDisease() != 0)
            list1.set(0, 0);
        if(requestComponent.getUserAllergy() != 0)
            list1.set(1, 1);
        if(requestComponent.getUserReligion() != 0)
            list1.set(2, 2);
        if(requestComponent.getUserVegan())
            list1.set(3, 3);
        List<Integer> list2 = this.tag.findallid();//requestComponent.getUserDisease());
        //System.out.println(list2.size());
        
        for (int i = 0; i < list1.size(); i++) {
            if(this.tag.findid(list1.get(i)).size() != 0)
            list2.retainAll(this.tag.findid(list1.get(i)));
        }
        //System.out.println(list2.get(9));
        //System.out.println(samples.size());

        for(int i = 0; i < list2.size(); i++){
            ResponseComponent response = new ResponseComponent();
            response.MenuId = samples.get(list2.get(i)-1).getMenuId();
            response.MenuName = samples.get(list2.get(i)-1).getMenuName();
            response.RestaurantName = samples.get(list2.get(i)-1).getRestaurantName();
            response.Img = samples.get(list2.get(i)-1).getImg();
            response.Carbo = samples.get(list2.get(i)-1).getCarbo();
            response.Protain = samples.get(list2.get(i)-1).getProtain();
            response.Lipid = samples.get(list2.get(i)-1).getLipid();
            response.TagId = this.tag.findtagid(samples.get(list2.get(i)-1).getMenuId());
            menus.add(response);
        }

        for (int i = 0; i < menus.size(); i++) {
            System.out.println(menus.get(i).MenuId);
            System.out.println(menus.get(i).MenuName);
            System.out.println(menus.get(i).RestaurantName);
            System.out.println(menus.get(i).Img);
            System.out.println(menus.get(i).Carbo);
            System.out.println(menus.get(i).Protain);
            System.out.println(menus.get(i).Lipid);
            System.out.println(menus.get(i).TagId);
        }
        
        //headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        
        //HttpEntity<Locationinfo> request = new HttpEntity<>(location.get(0).getName(), headers);
        //assertions.assertEquals(response.getStatusCode(), HttpStatus.CREATED);
        //System.out.println(url+location.get(1).getName());
        //food foods = new food();
        //return Requestai(/*restTemplate.getForObject(url+location.get(1).getName(),food.class)*/foods ,requestComponent);
        return menus;
    }
    //ai를 호출하는 부분
    public static String Requestai(food requestfood, RequestComponent requestComponent) {
        RestTemplate restTemplate = new RestTemplate();
        String url = "";
        ai aai = new ai();
        aai.food_name = requestfood.Menus;
        System.out.println(aai.food_name);
        
        HttpHeaders headers = new HttpHeaders();
        
        headers.setContentType(MediaType.APPLICATION_JSON);
        

        HttpEntity<ai> request = new HttpEntity<>(aai, headers);
        
    
        return restTemplate.postForObject(url, request,String.class);
    }

}
