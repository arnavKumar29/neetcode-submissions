class MinStack {
    Deque<Integer> st;
    Deque<Integer> tp;

    public MinStack() {
        st = new ArrayDeque<>();
        tp=new ArrayDeque<>();


        
    }
    
    public void push(int val) {
        st.push(val);
        if(tp.isEmpty()){
            tp.push(val);
        }else{
            tp.push(Math.min(val,tp.peek()));
        }
        
    }
    
    public void pop() {
        st.pop();
        tp.pop();
    }
    
    public int top() {
        return st.peek();
        
    }
    
    public int getMin() {
        return tp.peek();
        

        
        
    }
}
