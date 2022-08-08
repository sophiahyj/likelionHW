const $ = (selector) => document.querySelector(selector);
const openBtn = $(".openmodal_btn");
const closeBtn = $(".closemodal_btn");
const body = $("body");
const modal = $(".modal_container");

// function App() {
//   this.init = () => {
//     //스케줄 불러오는 함수를 호출해 첫 페이지 렌더링시 화면에 보여준다.
//     // 모달을 닫는 쿠키가 있는지 확인한다.
//     if(getCookie("modalClose") === "true") {
//       closeModal();
//       return;
//     }
//     // 모달을 닫는 쿠기가 없다면 무조건 모달을 열어둔다.
//     openModal();
//   };
// }
const openModal = () => {
  modal.classList.add("open");
  body.style.overflow = "hidden";
};

const closeModal = () => {
  modal.classList.remove("open");
  body.style.overflow = "auto";
};

openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);
$(".modal_container").addEventListener("click", (event) => {
  if (event.target === $(".modal_container")) {
    closeModal();
  };
});

const app = new App();
app.init();