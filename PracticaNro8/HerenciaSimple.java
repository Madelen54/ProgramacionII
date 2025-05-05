public class App{
    public static void main(String[] args){
        D o=new D(4,5,6);
        o.incrementaxyz();
        o.mostrar();
    
    }
}
class A{
    private int x;
    private int z;
    public A(int x , int z){
        this.x=x;
        this.z=z;
    }
    public void incrementaxz(){
        this.x+=1;
        this.z+=1;
    }
}
class B{
    public int y;
    public int z:


    public B(int y, int z){
        this.y=y;
        this.z=z;
    }
    public void incrementayz(){
        this.y+=1;
        this.z+=1;
    }
    public void incrementaz(){
        this.z+=1;
    }
    public int getY(){
        return y ;
    }
    public int getZ(){
        return z ;
    }
}
Interface IB{
    void incrementayz();
    void incrementaz
}
class D extends A implements IB{
    B objeto;
    public D(int x, int y , int z){
        super(x,z);
        this.objeto=new B(y,z);
    }
    public void incrementaxyz(){
        this.x+=1;
        this.objeto.incrementayz();
        this.z+=1;
    }
    public void incrementayz(){
        objeto.incrementayz();
    }
    public void incrementaz(){
        objeto.incrementaz();
    }
    public void mostrar(){
        System.out.println("x="+x);
        System.out.println("y="+objeto.getY());
        System.out.println("z="+z);
        System.out.println("z(B)="+objeto.getZ());
    }
}