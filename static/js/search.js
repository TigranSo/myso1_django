$('.inputSearch').on('input',function(){
     let value = this.value;
     if(value == ""){
         let filter = value.toUpperCase();

         let sections = $('section');
         for(let i = 0; i< sections.length; i++){
             sections[i].style.display="block";

         }
     }else{
         let filter = value.toUpperCase();

         let sections = $('section');
         console.log(sections);
         for(let i = 0; i< sections.length; i++){
             sections[i].style.display="block";
             if(!(sections[i].id.toUpperCase().indexOf(filter)>-1 )){

                 sections[i].style.display="none";
             }
         }
     }
//alert ("test");
 });


$('.test').on('change',function(){

    let value = this.value;
        let filter = value.toUpperCase();
        let sections = $('section');
        for(let i = 0; i< sections.length; i++){
            sections[i].style.display="block";
            if(!(sections[i].id.toUpperCase().indexOf(filter)>-1 )){

                sections[i].style.display="none";
            }
        }

 
});

$('.inputSearch1').on('input',function(){
     let value = this.value;
     if(value == ""){
         let filter = value.toUpperCase();

         let sections = $('section');
         for(let i = 0; i< sections.length; i++){
             sections[i].style.display="block";

         }
     }else{
         let filter = value.toUpperCase();

         let sections = $('section');
         console.log(sections);
         for(let i = 0; i< sections.length; i++){
             sections[i].style.display="block";
             if(!(sections[i].id.toUpperCase().indexOf(filter)>-1 )){

                 sections[i].style.display="none";
             }
         }
     }
//alert ("test");
 });


$('.test').on('change',function(){

    let value = this.value;
        let filter = value.toUpperCase();
        let sections = $('section');
        for(let i = 0; i< sections.length; i++){
            sections[i].style.display="block";
            if(!(sections[i].id.toUpperCase().indexOf(filter)>-1 )){

                sections[i].style.display="none";
            }
        }

 
});