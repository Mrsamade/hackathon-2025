const cardStack = document.querySelector(".card-stack");
const likeBtn = document.getElementById("like");
const nopeBtn = document.getElementById("nope");

function recordSwipe(swipedId, direction) {
  fetch("/swipe", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      swiper_id: 1, // TODO: replace with logged-in student id
      swiped_id: swipedId,
      direction: direction
    })
  }).catch((err) => {
    console.error("Failed to record swipe", err);
  });
}

function swipe(direction) {
  const topCard = cardStack.querySelector(".card:last-child");
  if (!topCard) return;

  const swipedId = topCard.dataset.id;
  recordSwipe(swipedId, direction);

  topCard.style.transform = `translateX(${
    direction === "like" ? 300 : -300
  }px) rotate(${direction === "like" ? 20 : -20}deg)`;
  topCard.style.opacity = 0;

  setTimeout(() => {
    topCard.remove();
  }, 300);
}

likeBtn.addEventListener("click", () => swipe("like"));
nopeBtn.addEventListener("click", () => swipe("nope"));
