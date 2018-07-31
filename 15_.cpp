/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>
#include <cstdio>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    	ListNode *newHead;
    	newHead.next = NULL;
    	ListNode curNode = newHead;

    	ListNode p = l1;
    	ListNode q = l2;

        while (l1 != NULL && l2 != NULL) {
        	if (l1.val > l2.val) {
        		curNode.next = p;
        		curNode = p;
        		p = p.next;
        	}
        	else {
        		curNode.next = q;
        		curNode = q
        		q = q.next;
        	}
        }

        while (!p) {
        	curNode.next = p;
        }
        while (!q) {
        	curNode.next = q;
        }
        return newHead.next;
    }
};