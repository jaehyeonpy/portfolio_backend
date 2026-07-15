package com.portfolio.controller;

import com.portfolio.service.VideoPersonalityFetchWithDefaultMongoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;



@RestController
@RequestMapping("/default-mongodb")
public class VideoPersonalityFetchWithDefaultMongoController {
    private final VideoPersonalityFetchWithDefaultMongoService videoPersonalityFetchWithDefaultMongoService;

    public VideoPersonalityFetchWithDefaultMongoController(
            VideoPersonalityFetchWithDefaultMongoService videoPersonalityFetchWithDefaultMongoService
    ) {
        this.videoPersonalityFetchWithDefaultMongoService = videoPersonalityFetchWithDefaultMongoService;
    }

    @GetMapping("/{videoPersonalityDocId}")
    public ResponseEntity<Map<String, Object>> getVideoPersonality(
            @PathVariable("videoPersonalityDocId") String videoPersonalityDocId
    ) {
        Map<String, Object> response =
                videoPersonalityFetchWithDefaultMongoService.fetchVideoPersonality(videoPersonalityDocId);
        return ResponseEntity.ok(response);
    }
}
