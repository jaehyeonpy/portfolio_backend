package com.portfolio.converter;

import org.bson.Document;
import org.springframework.stereotype.Component;

import java.util.LinkedHashMap;
import java.util.Map;



@Component
public class VideoPersonalityConverter {
    public Map<String, Object> convertDocumentToResponseMap(Document document) {
        return new LinkedHashMap<>(document);
    }
}
