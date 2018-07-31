#include <cstdio>
#include <iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if (head){
            ListNode *p = head;
            ListNode *q = head;
            int cur_val;

            while (p->next) {
                cur_val = p->next->val;
                ListNode *move_node = p->next;
                p->next = p->next->next;
                if (cur_val < head->val){  // first node
                    move_node->next = head;
                    head = move_node;
                }
                else {  // not first node
                    for (q = head; q->next && q->next->val < cur_val; q = q->next);
                    if (q->next->val == cur_val){
                        
                    }
                    
                    if (q->next){  // not the last
                        move_node->next = q->next;
                        q->next = move_node;
                    }
                    else {  // last node
                        q->next = move_node;
                        move_node->next = nullptr;
                    }
                }
                
            }
        }
        return head;
    }
};