package com.portfolio.controller;

import com.portfolio.service.VideoPersonalityFetchWithMongoConnectionPoolService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;



@RestController
@RequestMapping("/mongodb-connectionpool")
public class VideoPersonalityFetchWithMongoConnectionPoolController {
    private final VideoPersonalityFetchWithMongoConnectionPoolService videoPersonalityFetchWithMongoConnectionPoolService;

    public VideoPersonalityFetchWithMongoConnectionPoolController(
            VideoPersonalityFetchWithMongoConnectionPoolService videoPersonalityFetchWithMongoConnectionPoolService
    ) {
        this.videoPersonalityFetchWithMongoConnectionPoolService = videoPersonalityFetchWithMongoConnectionPoolService;
    }

    @GetMapping("/{videoPersonalityDocId}")
    public ResponseEntity<Map<String, Object>> getVideoPersonality(
            @PathVariable("videoPersonalityDocId") String videoPersonalityDocId
    ) {
        Map<String, Object> response =
                videoPersonalityFetchWithMongoConnectionPoolService.fetchVideoPersonality(videoPersonalityDocId);
        return ResponseEntity.ok(response);
    }
}
