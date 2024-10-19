
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")

    arr := []int{1, 2, 3}
    arr2 := []int{6, 3, 2, 1}
    fmt.Println(insertionSort(arr))
    fmt.Println(insertionSort(arr2))
}

func insertionSort(arr []int) []int {
    for i := 1; i < len(arr); i++ {
        j := i - 1
        for j >= 0 && arr[j] > arr[j + 1] {
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j--
        }
    }

    return arr
}

