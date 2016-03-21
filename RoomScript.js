var masterPoints = [];
//http://stackoverflow.com/questions/20916953/get-distance-between-two-points-in-canvas
//Posted by jaya
// point.IsMaster=0;
// point.signatureName='';
// point.heatSignature=0;
// point.Unit="Ferinheight";
// point.Humidity=0;
// point.x=0;
// point.y=0;

Math.dist=function(x1,y1,x2,y2){ 
  if(!x2) x2=0; 
  if(!y2) y2=0;
  return Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)); 
}
function test(){
	alert("test");
}

// function addHeatSignature (x,y,signatureName,) {
	
// 	point.IsMaster=0;
// 	point.signatureName='';
// 	point.heatSignature=0;
// 	point.Unit="Ferinheight";
// 	point.Humidity=0;
// 	point.x=0;
// 	point.y=0;

// }

function drawBoxes(canvas,horizontalSquares,VerticalSquares){

// var c=document.getElementById("myCanvas");
// var ctx=c.getContext("2d");
	var ctx = canvas.getContext("2d");
	X = horizontalSquares;
	Y = VerticalSquares;
	var xOffset = 0;
	var yOffset = 0;
	console.log("horizontalSquares: "+horizontalSquares);
	console.log("VerticalSquares: "+VerticalSquares);


	var dx = ((canvas.width) / (horizontalSquares));
	var dy = ((canvas.height) / (VerticalSquares));

	console.log("canvas.width: "+canvas.width);

	//Setup the default state.
	for (var j = 0; j<Y; j++) {
		xOffset = 0;
		for (var i = 0; i<X; i++) {
			console.log("xoff: "+xOffset+" yoff:"+yOffset+" dx:"+dx+" dy:"+dy);
			ctx.rect(xOffset,yOffset,dx,dy);
			xOffset += dx;
		}
		yOffset += dy;
	}
	ctx.stroke();
}