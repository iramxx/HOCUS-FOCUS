
document.addEventListener('DOMContentLoaded', () => {
    const wrapper = document.querySelector('.game-image-area');
    const scene = document.getElementById('scene');
    const canvas = document.getElementById('hint-canvas');
    const ctx = canvas.getContext('2d');
  
    // Dummy target in image-pixel coordinates (would come from API)
    const target = { x: 300, y: 200 };
    let misses = 0;
    let targetDiv;
  
    // Resize canvas to match image display
    function resizeCanvas() {
      canvas.width = scene.clientWidth;
      canvas.height = scene.clientHeight;
    }
    scene.addEventListener('load', resizeCanvas);
    window.addEventListener('resize', resizeCanvas);
  
    // Map image-space px to rendered-space px
    function toRenderCoords(imgX, imgY) {
      const scaleX = scene.clientWidth / scene.naturalWidth;
      const scaleY = scene.clientHeight / scene.naturalHeight;
      return { x: imgX * scaleX, y: imgY * scaleY };
    }
  
    // Initialize target overlay
    function createTargetDiv() {
      const pos = toRenderCoords(target.x, target.y);
      const size = 20; // hit area size
      targetDiv = document.createElement('div');
      Object.assign(targetDiv.style, {
        position: 'absolute',
        width: size + 'px',
        height: size + 'px',
        left: (pos.x - size/2) + 'px',
        top: (pos.y - size/2) + 'px',
        background: 'transparent',
        pointerEvents: 'auto',
        zIndex: 10,
      });
      // Handle correct click
      targetDiv.addEventListener('click', (e) => {
        e.stopPropagation();
        alert('✅ Correct!');
        clearHint();
        disableInteraction();
      });
      wrapper.appendChild(targetDiv);
    }
  
    // Draw a hint circle of given radius
    function drawHint(radius) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const pos = toRenderCoords(target.x, target.y);
      ctx.strokeStyle = 'rgba(255,0,0,0.6)';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, radius, 0, 2 * Math.PI);
      ctx.stroke();
    }
  
    // Clear the hint overlay
    function clearHint() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  
    // Disable further clicks
    function disableInteraction() {
      wrapper.style.pointerEvents = 'none';
    }
  
    // Handle miss on wrapper
    wrapper.addEventListener('click', () => {
      // determine hint radius based on miss count
      let radius;
      const maxDim = Math.max(canvas.width, canvas.height);
      if (misses === 0){
        radius = maxDim / 16;
        alert("❌ Incorrect. Look at the hint!")
      }      
      else if (misses === 1) radius = maxDim / 32;
      else {
        // final reveal: highlight the targetDiv
        clearHint();
        targetDiv.style.border = '3px solid rgba(255,0,0,0.8)';
        return;
      }
      drawHint(radius);
      misses++;
    });
  
    // Kick off
    resizeCanvas();
    createTargetDiv();
  });
  