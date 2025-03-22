import java.awt.Graphics;
import javax.swing.JPanel;
import javax.swing.JFrame;

class Punto {
    public double x, y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double[] coordCartesianas() {
        return new double[]{x, y};
    }

    public double[] coordPolares() {
        double radio = Math.sqrt(x * x + y * y);
        double angulo = Math.atan2(y, x);
        return new double[]{radio, angulo};
    }

  
    public String toString() {
        double[] polares = coordPolares();
        return String.format("Punto en coordenadas cartesianas: (%.2f, %.2f) - Polares: (r=%.2f, θ=%.3f rad)",
                x, y, polares[0], polares[1]);
    }
}

class Linea {
    public Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public double distancia() {
        return Math.sqrt(Math.pow(p2.getX() - p1.getX(), 2) + Math.pow(p2.getY() - p1.getY(), 2));
    }
    public String toString() {
        return String.format("La línea entre (%.2f,%.2f) y (%.2f,%.2f) tiene una distancia de: %.2f",
                p1.getX(), p1.getY(), p2.getX(), p2.getY(), distancia());
    }

    public void dibujarLinea(Graphics g) {
        g.drawLine((int) (p1.getX() * 50), (int) (p1.getY() * 50),
                   (int) (p2.getX() * 50), (int) (p2.getY() * 50));
    }
}

class Circulo {
    public Punto centro;
    public double radio;

    public Circulo(Punto centro, double radio) {
        this.centro = centro;
        this.radio = radio;
    }
    public String toString() {
        return String.format("Círculo con centro en (%.2f, %.2f) y radio %.2f",
                centro.getX(), centro.getY(), radio);
    }

    public void dibujarCirculo(Graphics g) {
        int x = (int) (centro.getX() * 50 - radio * 50);
        int y = (int) (centro.getY() * 50 - radio * 50);
        int diametro = (int) (radio * 2 * 50);
        g.drawOval(x, y, diametro, diametro);
    }
}

class Dibujo extends JPanel {
    public Linea linea;
    public Circulo circulo;

    public Dibujo(Linea linea, Circulo circulo) {
        this.linea = linea;
        this.circulo = circulo;
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        linea.dibujarLinea(g);
        circulo.dibujarCirculo(g);
    }
}
class Main{
    public static void main(String[] args) {
        Punto p1 = new Punto(1, 3);
        Punto p2 = new Punto(6, 5);

        Linea linea = new Linea(p1, p2);
        double radioCirculo = linea.distancia() / 2;
        Punto centroCirculo = new Punto((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2);

        Circulo circulo = new Circulo(centroCirculo, radioCirculo);

        System.out.println(linea);
        System.out.println(circulo);
        JFrame frame = new JFrame("Dibujo de Línea y Círculo");
        Dibujo dibujo = new Dibujo(linea, circulo);

        frame.add(dibujo);
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
