package services.websocket;

import com.lmax.disruptor.RingBuffer;
import services.disruptor.event.WebSocketEvent;
import org.java_websocket.WebSocket;
import org.java_websocket.handshake.ClientHandshake;
import org.java_websocket.server.WebSocketServer;

import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

public class HelloEndPoint extends WebSocketServer{
    private final RingBuffer<WebSocketEvent> ringBuffer;

    public HelloEndPoint(int port, RingBuffer<WebSocketEvent> ringbuffer) {
        super(new InetSocketAddress(port));
        this.ringBuffer = ringbuffer;
    }

    @Override
    public void onOpen(WebSocket webSocket, ClientHandshake clientHandshake) {
        System.out.println("opened");
    }

    @Override
    public void onClose(WebSocket webSocket, int i, String s, boolean b) {

    }

    @Override
    public void onMessage(WebSocket webSocket, String message) {
        ByteBuffer bb = ByteBuffer.wrap(message.getBytes());
        ringBuffer.publishEvent((event, sequence, buffer) -> {
            event.setValue(StandardCharsets.UTF_8.decode(buffer).toString());
            event.setWebsocket(webSocket);
        }, bb);
//        webSocket.send("Hello " + message);
    }

    @Override
    public void onError(WebSocket webSocket, Exception e) {

    }

    @Override
    public void onStart() {

    }
}

