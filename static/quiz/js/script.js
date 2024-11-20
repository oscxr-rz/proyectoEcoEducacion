// Lista de preguntas de cada categoría
let questions = [
    // Deforestación
    { id: 1, question: "¿Cuál es la principal causa de la deforestación en Ocotlán de Morelos?", options: ["La minería ilegal", "La expansión de la agricultura y ganadería", "El desarrollo urbano", "La reforestación masiva"], answer: 1 },
    { id: 2, question: "¿Qué tipo de vegetación predomina en Ocotlán de Morelos?", options: ["Selva tropical", "Bosques de pino-encino", "Sabana", "Bosques de manglar"], answer: 1 },
    { id: 3, question: "¿Cómo impacta la deforestación en la biodiversidad de la región?", options: ["Fomenta el crecimiento de nuevas especies", "Destruye hábitats naturales de especies como el jaguar y el quetzal", "No tiene impacto significativo", "Mejora la diversidad genética de las especies"], answer: 1 },
    { id: 4, question: "¿Qué consecuencias tiene la deforestación en el suelo de Ocotlán?", options: ["Mejora la fertilidad del suelo", "Aumenta la erosión y reduce la retención de agua", "Aumenta la cantidad de nutrientes en el suelo", "No tiene efectos negativos en el suelo"], answer: 1 },
    { id: 5, question: "¿Qué efecto tiene la deforestación sobre el cambio climático?", options: ["Contribuye al enfriamiento global", "Reduce el calentamiento global", "Aumenta las emisiones de carbono, agravando el calentamiento global", "No tiene impacto en el cambio climático"], answer: 2 },

    // Contaminación del Agua
    { id: 6, question: "¿Cuáles son las principales causas de la contaminación del agua en Ocotlán de Morelos, Oaxaca?", options: ["Actividades turísticas", "Vertidos industriales, uso de pesticidas y residuos sólidos", "Exceso de lluvias", "Uso exclusivo de agua potable para riego"], answer: 1 },
    { id: 7, question: "¿Qué efectos tiene la contaminación del agua en la salud pública de Ocotlán?", options: ["Mejoras en la salud pública", "Enfermedades respiratorias y problemas dermatológicos", "Enfermedades gastrointestinales y efectos tóxicos de metales pesados", "No tiene impacto en la salud"], answer: 2 },
    { id: 8, question: "¿Cómo impacta la contaminación del agua en la biodiversidad acuática de Ocotlán?", options: ["Aumento de especies acuáticas", "Disminución de la población de especies acuáticas", "No afecta la biodiversidad acuática", "Mejora el equilibrio ecológico de los ríos"], answer: 1 },
    { id: 9, question: "¿Qué tipo de industrias contribuyen a la contaminación del agua en Ocotlán?", options: ["Industrias farmacéuticas", "Industrias de procesamiento de caña de azúcar y pequeñas fábricas locales", "Solo la agricultura", "Industria textil"], answer: 1 },
    { id: 10, question: "¿Cuáles son las posibles soluciones para mejorar la calidad del agua en Ocotlán?", options: ["Construcción de más industrias", "Tratamiento de aguas residuales, agricultura sostenible y mejor manejo de residuos", "Prohibir el uso de pesticidas y fertilizantes", "Aumento de la urbanización"], answer: 1 },

    // Contaminación del Aire
    { id: 11, question: "¿Cuáles son las principales fuentes de contaminación del aire en Ocotlán de Morelos?", options: ["Solo el tráfico vehicular", "Las actividades agrícolas, el tráfico vehicular y las emisiones industriales", "Solo las actividades agrícolas", "Solo las emisiones de industrias locales"], answer: 1 },
    { id: 12, question: "¿Cómo afecta la contaminación del aire a la salud pública en Ocotlán de Morelos?", options: ["Mejora la salud pública", "No tiene impacto en la salud", "Aumenta enfermedades respiratorias y cardiovasculares", "Solo afecta a personas mayores"], answer: 2 },
    { id: 13, question: "¿Qué impacto tiene la contaminación del aire en los ecosistemas locales?", options: ["Mejora el equilibrio ecológico", "No tiene impacto en la biodiversidad", "Daña la vegetación y afecta los suelos", "Solo afecta a los ecosistemas marinos"], answer: 2 },
    { id: 14, question: "¿Qué medida podría reducir las emisiones contaminantes provenientes de la agricultura?", options: ["Aumentar la quema de residuos agrícolas", "Reducir la quema de residuos y usar tecnologías más limpias", "Incrementar el uso de pesticidas", "No tomar ninguna medida"], answer: 1 },
    { id: 15, question: "¿Qué soluciones se proponen para reducir la contaminación del aire causada por el tráfico vehicular en Ocotlán?", options: ["Aumentar el número de vehículos", "Mejorar el transporte público y promover el uso de vehículos eléctricos", "No tomar medidas sobre el tráfico", "Fomentar el uso exclusivo de transporte privado"], answer: 1 },

    // Explotación de Recursos Naturales
    { id: 16, question: "¿Cuál es la principal forma de explotación minera en Ocotlán de Morelos?", options: ["Minería subterránea", "Minería hidráulica", "Minería a cielo abierto", "Minería de sal"], answer: 2 },
    { id: 17, question: "¿Qué problemas ambientales ha causado la minería en Ocotlán de Morelos?", options: ["Solo contaminación del aire", "Deforestación, erosión del suelo y contaminación del agua", "Solo erosión del suelo", "Solo contaminación del aire y la tierra"], answer: 1 },
    { id: 18, question: "¿Cómo afecta la minería en la salud de la población local?", options: ["Mejora la salud de la población", "Causa intoxicaciones, problemas neurológicos y enfermedades respiratorias", "No tiene efectos en la salud", "Solo afecta la salud emocional de la población"], answer: 1 },
    { id: 19, question: "¿Qué tipo de minería se practica en la comunidad de San José del Progreso?", options: ["Minería subterránea", "Minería a cielo abierto", "Minería hidráulica", "Minería de carbón"], answer: 1 },
    { id: 20, question: "¿Cuáles son los principales conflictos sociales relacionados con la minería en San José del Progreso?", options: ["Apoyo unánime a los proyectos mineros", "Conflictos sociales por la falta de consulta y beneficios", "No existen conflictos sociales", "Total acuerdo entre la empresa minera y las comunidades"], answer: 1 },
];

let posActual = 0;
let cantidadAcertadas = 0;
let puntos = 0;
let respuestasUsuario = [];
let tiempoInicioPregunta;

// Barajar las preguntas y respuestas
let indices = Array.from(Array(questions.length).keys());
indices = indices.sort(() => Math.random() - 0.5);

// Tiempo por pregunta en segundos
const tiempoPregunta = 15;
let tiempoRestante = tiempoPregunta;
let intervalID;

function comenzarJuego() {
    // Reseteamos las variables
    posActual = 0;
    cantidadAcertadas = 0;
    puntos = 0;
    respuestasUsuario = [];
    tiempoRestante = tiempoPregunta;

    // Activamos las pantallas necesarias
    document.getElementById("pantalla-inicial").style.display = "none";
    document.getElementById("pantalla-juego").style.display = "block";
    cargarPregunta();
}

function cargarPregunta() {
    // Controlar si se acabaron las preguntas
    if (posActual >= questions.length) {
        terminarJuego();
    } else {
        limpiarOpciones();

        let idx = indices[posActual];
        let currentQuestion = questions[idx];

        // Barajar las opciones
        let shuffledOptions = currentQuestion.options.map((option, index) => ({ option, index }))
            .sort(() => Math.random() - 0.5);

        // Mostrar las opciones barajadas
        shuffledOptions.forEach((item, i) => {
            document.getElementById("n" + i).innerText = item.option;
            document.getElementById("n" + i).dataset.index = item.index;
        });

        // Actualizar el índice de la respuesta correcta
        currentQuestion.answer = shuffledOptions.findIndex(item => item.index === currentQuestion.answer);

        document.getElementById("pregunta").innerText = currentQuestion.question;

        // Reiniciar temporizador
        tiempoRestante = tiempoPregunta;
        clearInterval(intervalID);
        document.getElementById("tiempo").innerText = tiempoRestante;
        tiempoInicioPregunta = new Date().getTime();  // Guardar el tiempo de inicio de la pregunta
        intervalID = setInterval(actualizarTiempo, 1000);
    }
}

function limpiarOpciones() {
    document.getElementById("n0").className = "nombre";
    document.getElementById("n1").className = "nombre";
    document.getElementById("n2").className = "nombre";
    document.getElementById("n3").className = "nombre";

    document.getElementById("l0").className = "letra";
    document.getElementById("l1").className = "letra";
    document.getElementById("l2").className = "letra";
    document.getElementById("l3").className = "letra";
}

function actualizarTiempo() {
    tiempoRestante--;
    document.getElementById("tiempo").innerText = tiempoRestante;

    if (tiempoRestante <= 0) {
        clearInterval(intervalID);
        posActual++;
        setTimeout(cargarPregunta, 1000);
    }
}

function comprobarRespuesta(opElegida) {
    let idx = indices[posActual];
    let correcta = (opElegida == questions[idx].answer);
    let tiempoRespuesta = (new Date().getTime() - tiempoInicioPregunta) / 1000;  // Calcular el tiempo de respuesta en segundos

    respuestasUsuario.push(`${questions[idx].id},${correcta},${tiempoRespuesta}`);

    if (correcta) { // acertó
        document.getElementById("n" + opElegida).className = "nombre nombreAcertada";
        document.getElementById("l" + opElegida).className = "letra letraAcertada";
        cantidadAcertadas++;
        puntos += (tiempoRestante > 10) ? 5 : (tiempoRestante > 5) ? 3 : 1;
    } else { // no acertó
        document.getElementById("n" + opElegida).className = "nombre nombreNoAcertada";
        document.getElementById("l" + opElegida).className = "letra letraNoAcertada";

        // Resaltar la respuesta correcta
        document.getElementById("n" + questions[idx].answer).className = "nombre nombreAcertada";
        document.getElementById("l" + questions[idx].answer).className = "letra letraAcertada";
    }

    posActual++;
    document.getElementById("correctas").innerText = cantidadAcertadas;
    document.getElementById("puntos").innerText = puntos;
    clearInterval(intervalID);
    setTimeout(cargarPregunta, 1000);
}

function terminarJuego() {
    document.getElementById("pantalla-juego").style.display = "none";
    document.getElementById("pantalla-final").style.display = "block";
    document.getElementById("numCorrectas").innerText = cantidadAcertadas;
    document.getElementById("numIncorrectas").innerText = questions.length - cantidadAcertadas;
    document.getElementById("puntuacionFinal").innerText = puntos;

    document.getElementById("cantidadAcertadas").value = cantidadAcertadas;
    document.getElementById("respuestas").value = respuestasUsuario.join('|');
    document.getElementById("puntuacionForm").submit();
}
