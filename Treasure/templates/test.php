<html>
  <head>
    <style>
      .jacket {
  position: absolute;
  width: 7px;
  height: 7px;
  background-color: #e7d7c1;
  border-radius:50%;
  top:120px;
  left:137px;
  box-shadow: 0 20px #e7d7c1;
}

.jacket:before {
  content:"";
  position: absolute;
  width: 25px;
  height: 25px;
  background-color: #a78a7f;
  left:-10px;
  top:40px;
}

.jacket:after {
  content:"";
  position: absolute;
  border-top: 15px solid #8c1c13;
  border-right: 15px solid transparent;
  border-left: 15px solid transparent;
  width:0;
  height:0;
  top:40px;
  left:-12px;
}
.hat {
  position: absolute;
  width: 60px;
  height: 15px;
  border-radius:20px 20px 0 0; 
  background-color: #bf4342;
  top:80px;
  left:75px;
}

.hat:before {
  content:"";
  position: absolute;
  width: 40px;
  height: 20px;
  border-radius:10px 10px 0 0; 
  background-color: #bf4342;
  top:-20px;
  left:10px;
  box-shadow: inset 0 -5px #e7d7c1;
}

.hat:after {
  content:"";
  position: absolute;
  width: 40px;
  height: 100px;
  background-color: #735751;
  border-radius: 50% 60% 20% 20% / 70% 70% 20% 20%;
  top:20px;
  left:45px;
}

      </style>
</head>
<body>
<div class="door">
  <div class="door-front">
    <div class="knob"></div>
  </div>
  <div class="door-back">
    <div class="rack"></div>
    <div class="hat"></div>
    <div class="jacket"></div>
  </div>
  <div class="door-mat"></div>
</div>
</body>

  </html>