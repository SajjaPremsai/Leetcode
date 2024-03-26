class Solution{
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode temp = list1, tempprev = temp;
        int i = 0;
        while (i < a) {
            tempprev = temp;
            temp = temp.next;
            i++;
        }
        if (a == b) {
            temp = temp.next;
            tempprev.next = list2;
            while (tempprev.next != null) {
                tempprev = tempprev.next;
            }
            tempprev.next = temp;
            return list1;
        } else {
            while (i < b) {
                temp = temp.next;
                i++;
            }
        }
        tempprev.next = list2;
        while (tempprev.next != null) {
            tempprev = tempprev.next;
        }
        tempprev.next = temp.next;
        return list1;

    }
}