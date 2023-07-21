via = 0;
vam = 0;
vab = 0;
vji = 0;
function VIA() {
    via++;
    alert("votaste por Isabel Agudelo " );
    document.getElementById('pantalla0').innerHTML = via;
    window.history.back();
}
function VAM() {
    vam++;
    alert("votaste por Andrea Monotoya" );
    document.getElementById('pantalla1').innerHTML = vam;
    window.history.back();

}
function VAB() {
    vab++;
    alert("votaste por Antonia Bustamante" );
    document.getElementById('pantalla2').innerHTML = vab;
    window.history.back();

}
function VJI() {
    vji++;
    alert("votaste por Juan Isaza");
    document.getElementById('pantalla3').innerHTML = vji;
    window.history.back();
}