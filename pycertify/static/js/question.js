function resposta(){
    let resposta = document.getElementsByClassName("active");
    let btn = document.getElementById("resposta");
    let btn_next = document.getElementById("next_question");
    let array_btn_next = btn_next.action.split("/")
    let num_question = array_btn_next[array_btn_next.length-1]
    btn.action = "resposta/"+(parseInt(num_question)-1)+'/'+resposta[0].name
}