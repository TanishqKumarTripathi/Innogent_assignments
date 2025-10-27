import java.util.concurrent.Semaphore;

class Praking_lot {
    private final Semaphore parkinglot = new Semaphore(3);

    public void parkinglots(String carName) {
        try {
            System.out.println(carName + " Is trying to park");
            System.out.println();
            Thread.sleep(1000);
            parkinglot.acquire();
            System.out.println(carName + " parking !!!!");
            System.out.println();
            Thread.sleep(3000);

            System.out.println(carName + " Is exiting");
            System.out.println();
            parkinglot.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class Car extends Thread {
    private final Praking_lot parks;
    private final String Carname;

    public Car(Praking_lot parks, String Carname) {
        this.parks = parks;
        this.Carname = Carname;
    }

    public void run() {
        parks.parkinglots(Carname);
    }
}

public class Parking {
    public static void main(String args[]) throws InterruptedException {

        Praking_lot parks = new Praking_lot();
        for (int i = 1; i <= 10; i++) {
            Thread.sleep(500);
            Car cars = new Car(parks, "Carname" + i);
            cars.start();
        }

    }
}

