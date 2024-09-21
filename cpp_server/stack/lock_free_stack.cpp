#include <atomic>
#include <memory>
#include <thread>
#include <iostream>
#include <vector>

struct stack_value {
    std::thread::id tid;
    int val;
};

template<typename T>
class lock_free_stack {
    struct Node {
        std::shared_ptr<T> data;
        Node* next;

        Node(const T& _data): data(std::make_shared<T>(_data)){
        }
    };

    std::atomic<Node*> head;

public:
    void push(const T& data){
        Node* new_node = new Node(data);
        new_node->next = head.load();
        while(!head.compare_exchange_weak(new_node->next, new_node));
    }

    std::shared_ptr<T> pop(){
        Node* old_head = head.load();
        while(old_head && !head.compare_exchange_weak(old_head, old_head->next));
        return old_head ? old_head->data : nullptr;
    }
};

int main(){
    lock_free_stack<stack_value> s;
    auto push_f = [&](){
        for(int i = 0; i < 10; ++i){
            stack_value sv;
            sv.tid = std::this_thread::get_id();
            sv.val = i;
            s.push(sv);
        }
    };

    auto pop_f = [&](){
        for(int i = 0; i < 5; ++i){
            s.pop();
        }
    };

    std::vector<std::thread> threads;
    for(int i = 0; i < 5; ++i){
        threads.push_back(std::thread(push_f));
    }

    for(int i = 0; i < 5; ++i){
        threads.push_back(std::thread(pop_f));
    }

    for(std::thread& t: threads){
        t.join();
    }

    std::shared_ptr<stack_value> sv;
    while(sv=s.pop()){
        std::cout << "thread " << sv->tid << ":" << sv->val << std::endl;
    }

    std::cout << "finished" << std::endl;
    return 0;
}