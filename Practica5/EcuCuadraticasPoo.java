package practica2poo;
/**
 * obtener la solucion de una ecuacion cuadratica
 * Programa Poo
 * @author ESCARLET*
 * 22/03/25
 */
import java.util.Scanner; 

public class EcuacionCuadratica {
	private int a;
    private int b;
    private int c;

    public EcuacionCuadratica(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getDiscriminante() {
        return Math.pow(this.b, 2) - 4 * this.a * this.c;
    }

    public String getRaiz1() {
        double discriminante = getDiscriminante();
        if (discriminante < 0) {
            return "La ecuación no tiene soluciones reales.";
        } else if (discriminante == 0) {
            double x = -this.b / (2.0 * this.a);
            return String.format("La ecuación tiene una solución real: x = %.2f", x);
        } else {
            return getRaiz2(); 
        }
    }

    public String getRaiz2() {
        double discriminante = getDiscriminante();
        if (discriminante < 0) {
            return "La ecuación no tiene soluciones reales.";
        } else {
            double x1 = (-this.b + Math.sqrt(discriminante)) / (2.0 * this.a);
            double x2 = (-this.b - Math.sqrt(discriminante)) / (2.0 * this.a);
            return String.format("La ecuación tiene dos soluciones reales: x1 = %.2f, x2 = %.2f", x1, x2);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el valor de a: ");
        int a = scanner.nextInt();
        
        System.out.print("Ingrese el valor de b: ");
        int b = scanner.nextInt();
        
        System.out.print("Ingrese el valor de c: ");
        int c = scanner.nextInt();
        
        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);
        
        System.out.println("La discriminante es: " + ecuacion.getDiscriminante());
        System.out.println(ecuacion.getRaiz1());
    }
}
