<template>
    <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 64 64"
    width="24"
    height="24">
    <!-- Handle -->
    <rect x="20" y="4" width="8" height="24" fill="#d1b08a" />
    <!-- Blade -->
    <rect x="12" y="28" width="24" height="28" fill="#f2c094" />
    <!-- Edges -->
    <line x1="20" y1="4" x2="16" y2="28" stroke="black" stroke-width="2"/>
    <line x1="28" y1="4" x2="32" y2="28" stroke="black" stroke-width="2"/>
    <!-- Details on Blade -->
    <line x1="20" y1="28" x2="20" y2="56" stroke="black" stroke-width="2"/>
    <line x1="28" y1="28" x2="28" y2="56" stroke="black" stroke-width="2"/>
    <!-- Ball -->
    <circle cx="40" cy="20" r="6" fill="red" stroke="black" stroke-width="2"/>
  </svg>
  </template>
  
  <script>
  export default {
    name: 'CricketBatIcon',
  }
  </script>
  