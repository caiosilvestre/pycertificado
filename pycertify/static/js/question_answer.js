function resposta(){
    let resposta = document.getElementsByClassName("active");
    let btn = document.getElementById("resposta");
    let btn_next = document.getElementById("next_question");
    let array_btn_next = btn_next.action.split("/")
    let num_question = array_btn_next[array_btn_next.length-1]
    btn.action = "resposta/"+num_question+'/'+resposta[0].name
}
function traducao(){
    let switch_idioma = document.getElementsByClassName('form-check-input')[0] ;
    let label_idioma = document.getElementsByClassName("form-check-label")[0]
    console.log(switch_idioma)
    if(switch_idioma.checked){
        console.log('checked')
        label_idioma.innerHTML = "PT";
    }
    else{
        label_idioma.innerHTML = "EN"
    }
}