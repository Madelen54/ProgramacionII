public class Cola {
    private long arreglo[];
    private int inicio;
    private int fin;
    private int n;

    public Cola(int n){
        this.arreglo = new long[n+1];
        this.inicio = 0;
        this.fin = 0;
        this.n = n;
    }

    public void insert(long e){
        if(this.fin == n){
            System.out.println("Cola llena");
        }else{
            this.fin = this.fin +1;
            this.arreglo[this.fin] = e;
        }
    }

    public long remove(){
        if(this.inicio == 0 && this.fin == 0){
            System.out.println("Cola vacia");
            return -1;
        }else{
            this.inicio = this.inicio + 1;
            long dato = this.arreglo[this.inicio];

            if(this.inicio == this.fin){
                this.inicio = 0;
                this.fin = 0;
            }
            return dato;
        }
    }

    public long peek(){
        return this.arreglo[this.inicio+1];
    }

    public boolean isEmpty(){
        if(this.inicio == 0 && this.fin == 0){
            return true;
        }else{
            return false;
        }
    }

    public boolean isFull(){
        if(this.fin == this.n){
            return true;
        }else{
            return false;
        }
    }

    public int size(){ 
        return this.fin - this.inicio;
    }
    public static void main(String[] args) {
        Cola cola = new Cola(6);
        cola.insert(10001);
        cola.insert(28358);
        cola.insert(382176);
        cola.insert(4234);
        cola.insert(512634);
        cola.insert(73805);
        cola.insert(24892);

        while(! cola.isEmpty()){
            System.out.println(cola.remove());
        }
    }
    
}
