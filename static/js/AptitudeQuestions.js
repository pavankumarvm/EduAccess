window.onload = (function(){
    // Functions
    function buildQuiz(){
      // variable to store the HTML output
      const output = [];
  
      // for each question...
      myQuestions.forEach(
        (currentQuestion, questionNumber) => {
  
          // variable to store the list of possible answers
          const answers = [];
  
          // and for each available answer...
          for(letter in currentQuestion.answers){
  
            // ...add an HTML radio button
            answers.push(
              `<label>
                <input type="radio" name="question${questionNumber}" value="${letter}">
                ${letter} :
                ${currentQuestion.answers[letter]}
              </label>`
            );
          }
  
          // add this question and its answers to the output
          output.push(
            `<div class="slide">
              <div class="question"> ${currentQuestion.question} </div>
              <div class="answers"> ${answers.join("")} </div>
            </div>`
          );
        }
      );
  
      // finally combine our output list into one string of HTML and put it on the page
      quizContainer.innerHTML = output.join('');
    }
  
    function showResults(){
  
      // gather answer containers from our quiz
      const answerContainers = quizContainer.querySelectorAll('.answers');
  
      // keep track of user's answers
      let numCorrect = 0;
  
      // for each question...
      myQuestions.forEach( (currentQuestion, questionNumber) => {
  
        // find selected answer
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
  
        // if answer is correct
        if(userAnswer === currentQuestion.correctAnswer){
          // add to the number of correct answers
          numCorrect++;
  
          // color the answers green
          answerContainers[questionNumber].style.color = 'green';
        }
        // if answer is wrong or blank
        else{
          // color the answers red
          answerContainers[questionNumber].style.color = 'red';
        }
      });
  
      // show number of correct answers out of total
      resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
    }
  
    function showSlide(n) {
      slides[currentSlide].classList.remove('active-slide');
      slides[n].classList.add('active-slide');
      currentSlide = n;
      if(currentSlide === 0){
        previousButton.style.display = 'none';
      }
      else{
        previousButton.style.display = 'inline-block';
      }
      if(currentSlide === slides.length-1){
        nextButton.style.display = 'none';
        submitButton.style.display = 'inline-block';
      }
      else{
        nextButton.style.display = 'inline-block';
        submitButton.style.display = 'none';
      }
    }
  
    function showNextSlide() {
      showSlide(currentSlide + 1);
    }
  
    function showPreviousSlide() {
      showSlide(currentSlide - 1);
    }
  
    // Variables
    const quizContainer = document.getElementById('quiz');
    const resultsContainer = document.getElementById('results');
    const submitButton = document.getElementById('submit');
    const myQuestions = [
       { 
        question: "1. Express a speed of 36 kmph in meters per second?",
        answers: {
          a: "10mps",
          b: "12mps",
          c: "14mps",
          d: "17mps",
        },
        correctAnswer: "a"
      },
      {
        question: "2. The speed of a train is 90 kmph. What is the distance covered by it in 10 minutes?",
        answers: {
          a: "15Kmph",
          b: "12Kmph",
          c: "10Kmph",
          d: "5Kmph",
        },
        correctAnswer: "a"
      },
      
      {
        question: "3. Some persons can do a piece of work in 12 days. Two times the number of these people will do half of that work in?",
        answers: {
          a: "3 days",
          b: "4 days",
          c: "6 days",
          d: "58 days",
        },
        correctAnswer: ""
  },
  
      {
        question: "4. A car covers a distance of 624 km in 6 ½ hours. Find its speed?",
        answers: {
          a: "104Kmph",
          b: "140Kmph",
          c: "104mph",
          d: "10.4Kmph",
        },
        correctAnswer: "a"
      },
      
      {
        question: "5. A and B complete a work in 6 days. A alone can do it in 10 days. If both together can do the work in how many days?",
        answers: {
          a: "3.75 days",
          b: "4 days",
          c: "5 days",
          d: "6 days",
        },
        correctAnswer: "a"
      },
      
      {
        question: "6. The radius of a circle is increased by 1%. Find how much % does its area increases?",
        answers: {
          a: "1.01%",
          b: "5.01%",
          c: "3.01%",
          d: "2.01%",
        },
        correctAnswer: "d"
      },
      
      {
        question: "7. In how many years does a sum of Rs. 5000 yield a simple interest of Rs. 16500 at 15% p.a.?",
        answers: {
          a: "22",
          b: "24",
          c: "25",
          d: "23",
        },
        correctAnswer: "a"
      },
      
      {
        question: "8. What number has a 5:1 ratio to the number 10?",
        answers: {
          a: "42",
          b: "50",
          c: "55",
          d: "62",
        },
        correctAnswer: "b"
      },
      
      {
      question: "9. The Element of an electric heater is made of____",
      answers: {
        a: "Nichrome",
        b: "Copper",
        c: "Aluminum",
        d: "None of these",
      },
      correctAnswer: "a"
      },
    
      {
      question: "10. One mega watt hour (MWH) is equal to",
      answers: {
        a: "3.6 × 103 joule",
        b: "3.6 × 104 joule",
        c: "3.6 × 107 joule",
        d: "3.6 × 109 joule",
      },
      correctAnswer: "d"
      },
  
  
      
        {
          question: "11. Primitive men evolved in _________.",
          answers: {
            a: "Africa",
            b: "America",
            c: "Australia",
            d: "India",
          },
          correctAnswer: "a"
        },
  
        
          {
            question: "12. Which of the following is inheritable?",
            answers: {
              a: "An altered gene in sperm",
              b: "An altered gene in testes",
              c: "An altered gene in Zygote",
              d: "An altered gene in udder cell",
            },
            correctAnswer: "c"
          },
      
          
            {
              question: "13. Theory of natural selection was proposed by_______.",
              answers: {
                a: "Charles Darwin",
                b: "Hugo de Vries",
                c: "Gregor Johann Mendel",
                d: "Jean Baptiste Lamarck",
              },
              correctAnswer: "a"
            },
      
            
              {
                question: "14. Somatic gene therapy_______.",
                answers: {
                  a: "affects sperm",
                  b: "affects egg",
                  c: "affects progeny",
                  d: "affects body cell",
                },
                correctAnswer: "d"
              },
      
              
                {
                  question: "15. The paternal and maternal genetic material which influences the traits is_____.",
                  answers: {
                    a: "RNA",
                    b: "m-RNA",
                    c: "DNA",
                    d: "t-RNA",
                  },
                  correctAnswer: "c"
                },
      
                
                  {
                    question: "16. The meat eaters who existed 1.5 million years ago were called ______.",
                    answers: {
                      a: "Homo habilis",
                      b: "Hominids",
                      c: "Homo erectus",
                      d: "Homo sapiens",
                    },
                    correctAnswer: "c"
                  },
      
                  
                    {
                      question: "17. The term vaccine was coined by______.",
                      answers: {
                        a: "Dr. Ian Wilmut",
                        b: "Edward Jenner",
                        c: "Charles Darwin",
                        d: "Alexander Flemming",
                      },
                      correctAnswer: "b"
                    },
      
                    
                      {
                        question: "18. _______ is called as ‘Father of Genetics’.",
                        answers: {
                          a: "Charles Darwin",
                          b: "Hugo de Vries",
                          c: "Gregor Johann Mendel",
                          d: "Jean Baptiste Lamarck",
                        },
                        correctAnswer: "c"
                      },
      
                      
                        {
                          question: "19. Antibiotics are chemical substances derived from microbes like_____",
                          answers: {
                            a: "Fungi, Algae",
                            b: "Fungi, Bacteria",
                            c: "Fungi, Virus",
                            d: "Bacteria, Algae",
                          },
                          correctAnswer: "b"
                        },
      
                        
                          {
                            question: "20. Biological computers will be developed using_______.",
                            answers: {
                              a: "Bio sensor",
                              b: "Gene",
                              c: "Bio-Chips",
                              d: "Enzymes",
                            },
                            correctAnswer: "c"
                          },
                          
                          {
                            question: "21. Solutions are classified into aqueous and non-aqueous solutions, based on______. ",
                            answers: {
                              a: "Nature of solute particles",
                              b: "Nature of solvent",
                              c: "Size of the particles",
                              d: "Thickness of solvent",
                            },
                            correctAnswer: "b"
                          },
                          
                          {
                            question: "22. The solvent used to prepare aqueous solutions is________.",
                            answers: {
                              a: "Water",
                              b: "benzene",
                              c: "kerosene",
                              d: "petrol",
                            },
                            correctAnswer: "a"
                          },
      
                          {
                            question: "23. A true solution does not show Tyndall effect, because of the______.",
                            answers: {
                              a: "Nature of solvent",
                              b: "Amount of solute",
                              c: "Size of the particles",
                              d: "Nature of solute",
                            },
                            correctAnswer: "c"
                          },
      
                          {
                            question: "24. Tyndall effect is exhibited by________.",
                            answers: {
                              a: "True solutions",
                              b: "Suspensions",
                              c: "Colloidal solutions",
                              d: "Crystals",
                            },
                            correctAnswer: "c"
                          },
      
                          {
                            question: "25. According to Henry’s Law, in gases, an increase in pressure increase______",
                            answers: {
                              a: "Solubility",
                              b: "saturation",
                              c: "volume",
                              d: "viscosity",
                            },
                            correctAnswer: "a"
                          },
      
                          {
                            question: "26. The Principle of Uncertainty was introduced by__________.",
                            answers: {
                              a: "Broglie",
                              b: "Avogadro",
                              c: "Heisenberg",
                              d: "Einstein",
                            },
                            correctAnswer: "c"
                          },
      
                          {
                            question: "27. Atomicity is given by__________. ",
                            answers: {
                              a: "Mass/molecular mass",
                              b: "Mass of the element",
                              c: "Molecular mass X atomic mass",
                              d: "Molecular mass / atomic mass",
                            },
                            correctAnswer: "d"
                          },
      
                          {
                            question: "28. Atoms of different elements possessing in the same atomic mass are called",
                            answers: {
                              a: "Isotopes",
                              b: "Isobars",
                              c: "Isomers",
                              d: "Molecules",
                            },
                            correctAnswer: "a"
                          },
      
                          {
                            question: "29. Blood is an example of ________.",
                            answers: {
                              a: "True solution",
                              b: "Colloidal solution",
                              c: "Saturated solution",
                              d: "Suspension",
                            },
                            correctAnswer: "b"
                          },
  
                          {
                            question: "30. Brownian movement explains the ______ property of colloidal solutions",
                            answers: {
                              a: "optical",
                              b: "electrical",
                              c: "kinetic",
                              d: "mechanical",
                            },
                            correctAnswer: "c"
                          },
                          
                          {
                            question: "31. Sea route to India was discovered by",
                            answers: {
                              a: "Columbus",
                              b: "Amundsen",
                              c: "Vasco–da–gama",
                              d: "None of these",
                            },
                            correctAnswer: "c"
                          },
      
                          {
                            question: "32. Which one of the following was the port city of the Indus Valley Civilisation?",
                            answers: {
                              a: "Harappa",
                              b: "Kalibangan",
                              c: "Lothal",
                              d: "Mohenjodara",
                            },
                            correctAnswer: "c"
                          },
      
                          {
                            question: "33. Rig Veda is believed by the historians to have been written when it was",
                            answers: {
                              a: "Stone Age",
                              b: "Copper Age",
                              c: "Bronze Age",
                              d: "Beginning of Iron Age",
                            },
                            correctAnswer: "d"
                          },
      
                          {
                            question: "34. Babar entered India for the first time through",
                            answers: {
                              a: "Sind",
                              b: "Punjab",
                              c: "Kashmir",
                              d: "Rajasthan",
                            },
                            correctAnswer: ""
                          },
      
                          {
                            question: "35. Mahabharata war took place in",
                            answers: {
                              a: "500 AD",
                              b: "900 BC",
                              c: "1000 BC",
                              d: "1200 BC",
                            },
                            correctAnswer: "b"
                          },
                          
                          {
                            question: "36. India derives its name from",
                            answers: {
                              a: "The Hindus",
                              b: "The Aryans",
                              c: "Lord Indra",
                              d: "The River Indus",
                            },
                            correctAnswer: "d"
                          },
                          
                          {
                            question: "37. Who introduced English in India?",
                            answers: {
                              a: "Lord Rippon",
                              b: "Lord Dalhousie",
                              c: "Lord Canning",
                              d: "Lord William Bentick",
                            },
                            correctAnswer: "d"
                          },
                          
                          {
                            question: "38. The quit India movement was started in the year",
                            answers: {
                              a: "1942",
                              b: "1945",
                              c: "1943",
                              d: "1939",
                            },
                            correctAnswer: "a"
                          },
                          
                          {
                            question: "39. Taj Mahal is on the banks of",
                            answers: {
                              a: "Tapti",
                              b: "Ganges",
                              c: "Jamuna",
                              d: "Cauvery",
                            },
                            correctAnswer: "c"
                          },
                          
                          {
                            question: "40. Panipat is modern ",
                            answers: {
                              a: "Delhi",
                              b: "Kurukshetra",
                              c: "Sonepat",
                              d: "Faridabad",
                            },
                            correctAnswer: "b"
                          },
      
  ];
  
    // Kick things off
    buildQuiz();
  
    // Pagination
    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");
    const slides = document.querySelectorAll(".slide");
    let currentSlide = 0;
  
    // Show the first slide
    showSlide(currentSlide);
  
    // Event listeners
    submitButton.addEventListener('click', showResults);
    previousButton.addEventListener("click", showPreviousSlide);
    nextButton.addEventListener("click", showNextSlide);
  })();
  