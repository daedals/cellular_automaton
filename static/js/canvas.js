const canvas = document.getElementById('paintCanvas');
const ctx = canvas.getContext('2d');
const ws = new WebSocket('ws://localhost:8000/ws');

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

let isDrawing = false;

function startDrawing(event) {
    isDrawing = true;
    draw(event);
}

function draw(event) {
    if (!isDrawing) return;

    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const color = [0, 0, 0]; // Drawing color (black)

    ctx.fillStyle = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
    ctx.fillRect(x, y, 1, 1);

    ws.send(JSON.stringify({ action: 'draw', x: Math.floor(x), y: Math.floor(y), color }));
}

function stopDrawing() {
    isDrawing = false;
}

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (data.action === 'get_canvas') {
        const canvasData = data.canvas;
        for (let y = 0; y < canvasData.length; y++) {
            for (let x = 0; x < canvasData[y].length; x++) {
                const color = canvasData[y][x];
                ctx.fillStyle = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
                ctx.fillRect(x, y, 1, 1);
            }
        }
    }
};

// Request initial canvas state
ws.onopen = function() {
    ws.send(JSON.stringify({ action: 'get_canvas' }));
};
