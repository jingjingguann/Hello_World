let serial;
let latestData = "waiting for data";


function setup() {
 createCanvas(windowWidth, windowHeight);
 print("BEGIN!");
 console.log("starting!");

 serial = new p5.SerialPort();

 serial.list();
 serial.open('/dev/tty.usbserial-1410');

 serial.on('connected', serverConnected);

 serial.on('list', gotList);

 serial.on('data', gotData);

 serial.on('error', gotError);

 serial.on('open', gotOpen);

 serial.on('close', gotClose);

 

 
}

function serverConnected() {
 print("Connected to Server");
}

function gotList(thelist) {
 print("List of Serial Ports:");

 for (let i = 0; i < thelist.length; i++) {
  print(i + " " + thelist[i]);
 }
}

function gotOpen() {
 print("Serial Port is Open");
}

function gotClose(){
 print("Serial Port is Closed");
 latestData = "Serial Port is Closed";
}

function gotError(theerror) {
 print(theerror);
}

function gotData() {
 let currentString = serial.readLine();
  trim(currentString);
 if (!currentString) return;
 console.log(currentString);
 latestData = currentString;

}

function draw() {
    background(0,0,0);
    //fill(latestData*2,latestData,latestData*2);
    text(latestData, 10, 10);
    noStroke();
    //first option
  for (let i = 0; i < 50; i++) {
    fill(0, latestData*2, 255, 255);
    ellipse(random(windowWidth), random(windowWidth), latestData*2,latestData*2); 
    
    //second option
    //fill(0, latestData/2, 255);
    //rect(200, 200, latestData*5, latestData*5);
    
    //fill(0, latestData, 255);
    //rect(200, 200, latestData*4, latestData*4);
    
    //fill(0, latestData*2, 255);
    //rect(200, 200, latestData*3, latestData*3);
    
    //fill(0, latestData*2+50, 255);
    //rect(200, 200, latestData*2, latestData*2);


    //third option
    //ellipse(350, 350, latestData*2,latestData*2);
}
}
    
 
    






    //lastestData=map(lastestData,0,1186,0,250);
    //if (lastestData == 0) {
   
        //ellipse(width / 2,height /2 ,100,100);
    //} else {
       // rectMode(CENTER);
       // rect(width / 2, height / 2,100,100);
       //let m = map(latestData, 0, 1184, 0, 550);
    
       //ellipse(850,100,latestData/2,latestData/2);
       //ellipse(10,100,latestData/2,latestData/2);
       //ellipse(700,200,latestData/3,latestData/2);
       //ellipse(latestData,latestData,50,50);
       //ellipse(1000,100,latestData/2,latestData/2);

       
    
