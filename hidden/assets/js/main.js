const dashboardTitle = document.getElementById('dashboardTitle');
const datePlaceholder = document.getElementById('datePlaceholder');
const pageLoadDate = document.getElementById('pageLoadDate');

(function ($) {
 'use strict';

 var fullHeight = function () {
  $('.js-fullheight').css('height', $(window).height());
  $(window).resize(function () {
   $('.js-fullheight').css('height', $(window).height());
  });
 };
 fullHeight();

 $('#sidebarCollapse').on('click', function () {
  $('#sidebar').toggleClass('active');
 });
})(jQuery);

// Function to update the date to the current time
function updateDate() {
 const currentDate = new Date();
 const options = {
  weekday: 'short',
  month: 'short',
  day: 'numeric',
  year: 'numeric',
 };
 const formattedDate = currentDate.toLocaleDateString('en-US', options);
 datePlaceholder.innerText = formattedDate;
 datePlaceholder.innerHTML = `<span style="font-weight: bold; color: #6c757d;">${formattedDate}</span>`;

 pageLoadDate.innerText = formattedDate;
 pageLoadDate.innerHTML = `<span style="font-weight: bold; color: #6c757d;">${formattedDate}</span>`;
 // dashboardTitle.innerText = `<span style="font-weight: bold; color: #6c757d"></spsn>`;
 dashboardTitle.style.color = '#6c757d';
 dashboardTitle.style.fontWeight = 'bold';
}

// Update the date when the page loads
updateDate();

// Update the date every 24 hours
// setInterval(updateDate, 24 * 60 * 60 * 1000);

// updates every seconds
setInterval(updateDate, 1000);
