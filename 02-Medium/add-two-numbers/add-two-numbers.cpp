// https://leetcode.com/problems/add-two-numbers/

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int value = 0;
        ListNode* pRoot = NULL;
        ListNode* pCur = NULL;

        while (l1 && l2) {
            value = l1->val + l2->val + value;
            AppendNode(pRoot, pCur, value%10);
            value /= 10;

            l1 = l1->next;
            l2 = l2->next;
        }

        l1 = l1 ? l1 : l2;

        while (l1) {
            value = l1->val + value;
            AppendNode(pRoot, pCur, value % 10);
            value /= 10;
            l1 = l1->next;
        }

        while (value > 0) {
            AppendNode(pRoot, pCur, value % 10);
            value /= 10;
        }

        return pRoot;
    }

    static void AppendNode(ListNode*& pRoot, ListNode*& pLast, int value)
    {
        if (nullptr == pRoot) {
            pRoot = new ListNode(value);
            pLast = pRoot;
        }
        else {
            pLast->next = new ListNode(value);
            pLast = pLast->next;
        }
    }

};