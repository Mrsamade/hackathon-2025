const cardStack = document.querySelector(".card-stack");
const likeBtn = document.getElementById("like");
const nopeBtn = document.getElementById("nope");

function swipe(direction) {
  const topCard = cardStack.querySelector(".card:last-child");
  if (!topCard) return;

  topCard.style.transform = `translateX(${direction === 'like' ? 300 : -300}px) rotate(${direction === 'like' ? 20 : -20}deg)`;
  topCard.style.opacity = 0;

  setTimeout(() => {
    topCard.remove();
  }, 300);
}

likeBtn.addEventListener("click", () => swipe("like"));
nopeBtn.addEventListener("click", () => swipe("nope"));
