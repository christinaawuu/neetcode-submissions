class DynamicArray {
public:

    DynamicArray(int capacity) {
        index = 0;
        size = capacity;
        if(capacity > 0)
            arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if(index == size)
            resize();

        arr[index] = n;
        index++;
    }

    int popback() {
        if(index > 0) 
            index -= 1;
        return arr[index];
    }

    void resize() {
        // index *= 2;
        size *= 2;
        int* copy = new int[size];
        for(int i = 0; i < index; i++)
        {
            copy[i] = arr[i];
        }
        
        arr = copy;
    }

    int getSize() {
        return index;
    }

    int getCapacity() {
        return size;
    }

private:
    int* arr;
    int size = 0;
    int index = 0; 
};
