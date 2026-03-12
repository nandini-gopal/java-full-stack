const students={name:'santhosh',age:'16',city:'hyd'};
//object destructing
const{nmae:fullname,age:years,city:palce}=students;
//default
const{country='india'}=students;
console.log(country);
//spread operator=individual elements
const a=[1,2,3,4];
console.log(a)
console.log(...a);
//combine arrays
let boys=['tony','bablu','dheeraj'];
let girls=['teddy','siri','ammu'];
let family=[...boys,...girls];
console.log(family);
//spread with objects
const colors={c1:'red',c2:'green',c3:'blue'};
const shape={s1:'circle',s2:'square'};
const combine={...colors,...shape};//if same key value it override
console.log(combine);