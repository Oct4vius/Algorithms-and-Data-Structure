function quickSort<T>( array: T[] ): T[]{

    if(array.length <= 1){
        return array
    }

    let less: T[] = []
    let greater: T[] = []
    let pivot: T = array[0]

    for(const element of array.splice(1)){
        if (element <= pivot){
            less.push(element)
        }else{
            greater.push(element)
        }
    }
    return [...quickSort<T>(less), pivot, ...quickSort<T>(greater) ]
}