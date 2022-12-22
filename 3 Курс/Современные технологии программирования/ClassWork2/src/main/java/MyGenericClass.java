public class MyGenericClass <T>{
    private T obj;
    MyGenericClass(T obj)
    {
        this.obj = obj;
    }
    public T getObj()
    {
        return obj;
    }
}
