package com.select_food.main.repository;


//import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
//import org.springframework.data.jpa.repository.Query;
//import org.springframework.data.repository.CrudRepository;
//import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.select_food.main.model.Locationinfo;
//import com.select_food.main.model.Menu;

@Repository
public interface LocationRepo extends JpaRepository<Locationinfo,String> {
    //@Query(" select r, ( 6371 * acos( cos( radians(:lat) ) * cos( radians( r.latitude ) ) * cos(radians( r.longitude ) - radians(:lng) ) + sin( radians(:lat) ) * sin( radians( r.latitude )))) AS distance FROM Locationinfo r HAVING distance <= 0.1 ORDER BY distance ASC ")
    /*@Query("SELECT r FROM Locationinfo r " +
       "WHERE (6371 * acos(cos(radians(:lat)) * cos(radians(r.latitude)) * cos(radians(r.longitude) - radians(:lng)) + sin(radians(:lat)) * sin(radians(r.latitude)))) <= 0.5 " +
       "ORDER BY (6371 * acos(cos(radians(:lat)) * cos(radians(r.latitude)) * cos(radians(r.longitude) - radians(:lng)) + sin(radians(:lat)) * sin(radians(r.latitude)))) ASC")
    List<Locationinfo> findByLatitudeAndLongitude(@Param("lat") Double lat, @Param("lng") Double lng);*/

}
