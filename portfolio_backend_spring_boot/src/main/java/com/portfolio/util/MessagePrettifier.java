package com.portfolio.util;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;



public class MessagePrettifier {
    private static final Logger MYAPP_LOGGER = LoggerFactory.getLogger("myapp");

    private final String errorPrintMode;
    private final ObjectMapper objectMapper = new ObjectMapper();

    public MessagePrettifier(String errorPrintMode) {
        this.errorPrintMode = errorPrintMode;
    }

    public Object prettifyJson(Object data) {
        try {
            return objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(data);
        } catch (Exception e) {
            if ("printingToLog".equals(errorPrintMode)) {
                MYAPP_LOGGER.error("an error occured. returning the msg as it is.", e);
            } else if ("printingToConsole".equals(errorPrintMode)) {
                System.out.println("an error occured. returning the msg as it is.");

                Throwable current = e;
                while (current != null) {
                    System.out.println(current);

                    for (StackTraceElement element : current.getStackTrace()) {
                        System.out.println("\tat " + element);
                    }

                    current = current.getCause();
                    if (current != null) {
                        System.out.println("Caused by:");
                    }
                }
            }

            return data;
        }
    }
}
