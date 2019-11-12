#include <iostream>

struct Node {
    /*
        Using a Struct instead of a class because all members here are public, because they need to be accessible to the 'SingleLinkedList' class
    */
    int value;
    Node *next = nullptr;

    Node(int value) {
        this -> value = value;
    }

};

class SingleLinkedList {
    Node * head = nullptr;
    int size = 0;

    public:

        void add(int value) {

            if (size == 0) {
                this -> head = new Node(value);
            }
            else {
                Node *node = this -> head;
                while (node -> next != NULL)
                {
                    node = node -> next;
                }
                Node *new_node = new Node(value);
                new_node -> value = value;
                node -> next = new_node;
            }
            this-> size++;
        }

        void remove() {
            assert(this -> size != 0);

            Node *node = this -> head;
            while (node -> next -> next != NULL) {
                node = node -> next;
            }
            node -> next = NULL;
            this -> size--;
        }

        void traverse_nodes() {
            Node *node = this -> head;
            while (node != NULL) {
                std::cout << node -> value << "\n";
                node = node -> next;
            }
        }
};

int main() {
    SingleLinkedList x =  SingleLinkedList();
    x.add(12);
    x.add(15);
    x.add(27);
    x.remove();
    x.traverse_nodes();
    std::cout <<"Hello CPP, World!";
    return 0;
}