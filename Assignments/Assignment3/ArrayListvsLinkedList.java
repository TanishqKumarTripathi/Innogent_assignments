import java.util.*;

public class alvsll {

    public static long arraylist(ArrayList<Integer> al, int n) {

        long start_time = System.nanoTime();
        for (int i = 0; i < n; i++) {
            al.add(i);
        }
        long end_time = System.nanoTime();
        long total_time = end_time - start_time;
        return total_time;
    }

    public static long arraylist_remove(ArrayList<Integer> al) {
        // int n = 10000;
        long start_time = System.nanoTime();
        for (int i = 0; i < al.size(); i++) {
            al.remove(i);
        }
        long end_time = System.nanoTime();
        long total_time = end_time - start_time;

        return total_time;
    }

    public static long linkedlist(LinkedList<Integer> ll, int n) {

        long start_time = System.nanoTime();
        for (int i = 0; i < n; i++) {
            ll.add(i);
        }
        long end_time = System.nanoTime();
        long total_time = end_time - start_time;

        return total_time;
    }

    public static long linkedlist_remove(LinkedList<Integer> ll) {

        Iterator<Integer> it = ll.iterator();
        long start_time = System.nanoTime();
        while (it.hasNext()) {
            it.next();
            it.remove();
        }
        long end_time = System.nanoTime();
        long total_time = end_time - start_time;

        return total_time;
    }

    public static void main(String[] args) {

        ArrayList<Integer> al = new ArrayList<>();
        LinkedList<Integer> ll = new LinkedList<>();

        int[] size = { 10000, 50000, 100000 };
        for (int n : size) {
            System.out.println("For size: " + n);
            long arraylist_time = arraylist(al, n);
            long linkedlist_time = linkedlist(ll, n);

            long arraylist_remove_time = arraylist_remove(al);
            long linkedlist_remove_time = linkedlist_remove(ll);

            System.out
                    .println("Time taken by ArrayList to insert: " + (float) arraylist_time / 1000000000 + " Seconds");

            System.out.println(
                    "Time taken by LinkedList to insert: " + (float) linkedlist_time / 1000000000 + " Seconds");

            if (arraylist_time < linkedlist_time) {
                System.out.println(
                        "ArrayList is faster than LinkedList by "
                                + (float) (linkedlist_time - arraylist_time) / 1000000000
                                + " Seconds");
            } else if (linkedlist_time < arraylist_time) {
                System.out.println(
                        "LinkedList is faster than ArrayList by "
                                + (float) (arraylist_time - linkedlist_time) / 1000000000
                                + " Seconds");
            } else {
                System.out.println("Both are equal in time");
            }

            System.out.println(
                    "Time taken by ArrayList to remove: " + (float) arraylist_remove_time / 1000000000 + " Seconds");
            System.out
                    .println("Time taken by LinkedList to remove: " + (float) linkedlist_remove_time / 1000000000
                            + " Seconds");

            if (arraylist_remove_time < linkedlist_remove_time) {
                System.out.println("ArrayList is faster than LinkedList in removing by "
                        + (float) (linkedlist_remove_time - arraylist_remove_time) / 1000000000 + " Seconds");
            } else if (linkedlist_remove_time < arraylist_remove_time) {
                System.out.println("LinkedList is faster than ArrayList in removing by "
                        + (float) (arraylist_remove_time - linkedlist_remove_time) / 1000000000 + " Seconds");
            } else {
                System.out.println("Both are equal in time for removing");
            }
        }
    }
}
