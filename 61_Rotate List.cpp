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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) {
            return NULL;
        }
        // get the length of linked list
        int length = 1;
        ListNode *pNode = head;
        while (pNode->next) {
            length++;
            pNode = pNode->next;
        }
        ListNode *lastNode = pNode;
        k = k % length;  // if k > length, calculate the modulus

        if (k == 0){
            return head;
        }
        
        ListNode *preCutNode = head;
        
        for (int i = 0; i < length - k - 1; i++){  // need to cut the list between preCutNode and preCutNode->next
            preCutNode = preCutNode->next;
        }

        // rearrange the list
        lastNode->next = head;
        ListNode *newHead = preCutNode->next;
        preCutNode->next = NULL;

        return newHead;

    }
};