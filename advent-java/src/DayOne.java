import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class DayOne {
    public static void main(String[] args) throws IOException {
        String filePath = "/Users/ianlayzer/Desktop/advent/1.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        List<Integer> lines = new ArrayList<>();
        String currentLine;
        while ((currentLine = br.readLine()) != null) {
            lines.add(Integer.parseInt(currentLine.strip()));
        }
        System.out.println(lines.toString());
    }
}

