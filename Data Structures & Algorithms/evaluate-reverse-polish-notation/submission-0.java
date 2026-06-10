class Solution {
    public int evalRPN(String[] tokens) {
        int n = tokens.length;
        Deque<Integer> st = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            if (!tokens[i].equals("*") && !tokens[i].equals("+")
                    && !tokens[i].equals("-") && !tokens[i].equals("/")) {

                st.push(Integer.parseInt(tokens[i]));
            } else {

                if (tokens[i].equals("+") && st.size() >= 2) {
                    int b = st.pop();
                    int a = st.pop();
                    int c = a + b;
                    st.push(c);
                }

                if (tokens[i].equals("-") && st.size() >= 2) {
                    int b = st.pop();
                    int a = st.pop();
                    int c = a - b;
                    st.push(c);
                }

                if (tokens[i].equals("*") && st.size() >= 2) {
                    int b = st.pop();
                    int a = st.pop();
                    int c = a * b;
                    st.push(c);
                }

                if (tokens[i].equals("/") && st.size() >= 2) {
                    int b = st.pop();
                    int a = st.pop();
                    int c = a / b;
                    st.push(c);
                }
            }
        }

        return st.peek();
    }
}