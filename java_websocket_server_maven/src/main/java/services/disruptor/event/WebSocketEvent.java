package services.disruptor.event;

import org.java_websocket.WebSocket;

public class WebSocketEvent {
    private String value;
    private WebSocket websocket;

    public void setValue(String value) {
        this.value = value;
    }

    public void setWebsocket(WebSocket websocket) {
        this.websocket = websocket;
    }

    public WebSocket getWebsocket() {
        return websocket;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return "StringEvent{" + value + "}";
    }
}
