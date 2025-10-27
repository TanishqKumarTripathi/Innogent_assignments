import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

class pc_class {
    int n;
    ArrayList<Integer> al = new ArrayList<>(n); //bucket
    boolean stop; //flag variable

    public pc_class(int n) {
        this.n = n;
    }

    public void producer() throws InterruptedException {
        int value = 0;
        System.out.println("Excecution Started Successfully!!!");
        while (!stop) {
            synchronized (this) {
                if (al.size() == n) {
                    System.out.println("Bucket is full!!!");
                    wait();
                }
                // case to stop the execussion of both the threads when val reaches 10; 
                if (value == 10) {
                    System.out.println("Execution stopped");
                    stop = true;
                    notify();
                    break;
                }
                al.add(value);
                System.out.println(Thread.currentThread().getName() + " " + value + " added in the current bucket!!!");
                value++;
                notify();
                Thread.sleep(2000);
            }
        }
    }

    public void consumer() throws InterruptedException {
        while (!stop) {
            synchronized (this) {
                if (al.isEmpty()) {
                    System.out.println("Bucket is Empty!!!");
                    notify();
                    wait();
                }

                int val = al.remove();
                System.out.println(Thread.currentThread().getName() + "consumed: " + val);
                notify();

                Thread.sleep(2000);

            }
        }
        System.out.println("Excecution Completed Successfully!!!");
    }
}

public class Producer_Consumer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        while (true) {
            try {
                System.out.println("Enter number of productions: ");
                n = sc.nextInt();
                if (n <= 0) {
                    throw new InputMismatchException();
                }
                break;
            } catch (Exception e) {
                System.out.println("Enter a number greater than ZERO!!!");
            }
            sc.nextLine();
        }
        pc_class pc = new pc_class(n);

        Thread t1 = new Thread(new Runnable() {
            public void run() {
                try {
                    pc.producer();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        t1.setName("Producer");

        Thread t2 = new Thread(new Runnable() {
            public void run() {
                try {
                    pc.consumer();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        t2.setName("Consumer");

        t1.start();
        t2.start();
    }
}


