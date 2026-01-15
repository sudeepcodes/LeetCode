/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //edgecase

    if(head==NULL)
    return head;


    Node *prev=new Node();
    Node *curr=head;
   Node *temp;
//       1->2->3->4->null
//prev   c t

   while(curr!=NULL)
   { 
    temp=curr->next;
    curr->next=prev;
    prev=curr;
    curr=temp;
   }

return head;





    }
    
};