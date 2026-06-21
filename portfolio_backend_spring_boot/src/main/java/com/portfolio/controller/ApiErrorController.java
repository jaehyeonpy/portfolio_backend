package com.portfolio.controller;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.http.HttpServletRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;



@RestController
public class ApiErrorController implements ErrorController {
    private static final Logger log = LoggerFactory.getLogger("myapp");

    @RequestMapping("/error")
    public ResponseEntity<Void> handleError(HttpServletRequest request) {
        log.error(
                "API error. method={}, uri={}, status={}, message={}",
                request.getMethod(),
                request.getAttribute(RequestDispatcher.ERROR_REQUEST_URI),
                request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE),
                request.getAttribute(RequestDispatcher.ERROR_MESSAGE)
        );

        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
