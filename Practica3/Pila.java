public class Pila {
    private float arreglo[]; 
    private int top ;
    private int n;
    
    public Pila(int n){
        this.top=0;
        this.n=n;
        arreglo=new float[n+1];
    }
    public void push(float e){
        this.top=this.top+1;
        arreglo[this.top]=e;
    }
    public float pop(){
        float dato=arreglo[this.top];
        this.top=this.top-1;
        return dato;
    }
    public float peek(){
        return arreglo[this.top];
    }
    public boolean isEmpty(){
        if(this.top==0){
            return true;
        }else{
            return false;
        }   
    }
    public boolean isFull(){
        if(this.top==n){
            return true;
        }
        else{
            return false;
        }
    }
}
