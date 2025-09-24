document.getElementById("current-year").textContent = new Date().getFullYear();

const mobileMenuToggle = document.querySelector(".mobile-menu-toggle");
const sidebar = document.querySelector(".sidebar");
const sidebarOverlay = document.querySelector(".sidebar-overlay");
const sidebarClose = document.querySelector(".sidebar-close");
const sidebarLinks = document.querySelectorAll(".sidebar-nav a");

function openSidebar() {
  sidebar.classList.add("active");
  sidebarOverlay.classList.add("active");
  document.body.style.overflow = "hidden";
}

function closeSidebar() {
  sidebar.classList.remove("active");
  sidebarOverlay.classList.remove("active");
  document.body.style.overflow = "";
}

mobileMenuToggle.addEventListener("click", openSidebar);
sidebarClose.addEventListener("click", closeSidebar);
sidebarOverlay.addEventListener("click", closeSidebar);

sidebarLinks.forEach((link) => {
  link.addEventListener("click", closeSidebar);
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && sidebar.classList.contains("active")) {
    closeSidebar();
  }
});
