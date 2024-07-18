const strings = ['s', 'b', 'c', 'd']


//O(1)
//searches for index
strings[1]

//O(1) 
//adds element to the end
strings.push('e')

//O(1)
//removes last element
strings.pop()


//O(n)
//moves every element one over to place in first slot. iterates through
strings.unshift('x')

//O(n)
//moves elements over to place in middle. worst case is O
strings.splice(2, 0, 'z')