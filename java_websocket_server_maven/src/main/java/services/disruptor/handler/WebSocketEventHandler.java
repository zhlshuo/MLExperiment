package services.disruptor.handler;

import com.lmax.disruptor.EventHandler;
import services.disruptor.event.WebSocketEvent;

public class WebSocketEventHandler implements EventHandler<WebSocketEvent> {
    @Override
    public void onEvent(WebSocketEvent event, long sequence, boolean endOfBatch) {
        System.out.println("Event: " + event);
        event.getWebsocket().send("Hello " + event.getValue());
    }
}