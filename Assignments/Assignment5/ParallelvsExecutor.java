import java.util.stream.*;
import java.util.*;
import java.util.concurrent.*;

public class ParallelvsExecutor {

    public static void main(String args[]) throws InterruptedException, ExecutionException {
        int size = 100;

        long start = System.currentTimeMillis();

        long sum1 = IntStream.range(0, size)
                .parallel()
                .mapToLong(x -> (long) x * x)
                .sum();

        long end = System.currentTimeMillis();

        System.out.println("Sum: " + sum1);
        System.out.println("Time used by parallel stream: " + (end - start));

        int numthreads = Runtime.getRuntime().availableProcessors();
        ExecutorService executor = Executors.newFixedThreadPool(numthreads);

        int chunk_size = size / numthreads;
        List<Future<Long>> future = new ArrayList<>();

        long start1 = System.currentTimeMillis();
        System.out.println("Number of threads " + numthreads);
        System.out.println("chunk size " + chunk_size);

        for (int i = 0; i < numthreads; i++) {
            int start2 = i * chunk_size;
            int end2 = (i == numthreads - 1) ? size : start2 + chunk_size;
            System.out.println("Thread " + (i + 1) + " processing from " + start2 + " to " + (end2 - 1));

            future.add(executor.submit(() -> {
                long localsum = 0;
                for (int j = start2; j < end2; j++) {
                    localsum += (long) j * j;
                }
                return localsum;
            }));
        }

        long total_sum = 0;
        for (Future<Long> f : future) {
            total_sum += f.get();
        }

        long end1 = System.currentTimeMillis();
        executor.shutdown();

        System.out.println("Total Sum " + total_sum);
        System.out.println("Time used by executor: " + (end1 - start1));

        int cores = Runtime.getRuntime().availableProcessors();
        System.out.println("/Available cpu cores " + cores);
        System.out.println("Threads count " + Thread.activeCount());

    }
}

