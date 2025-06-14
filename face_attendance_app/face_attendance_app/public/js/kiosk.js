(async () => {
    const video = document.getElementById('video');
    const status = document.getElementById('status');
    const btn = document.getElementById('checkin-btn');

    if (navigator.mediaDevices.getUserMedia) {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
    }

    btn.addEventListener('click', async () => {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0);
        const dataUrl = canvas.toDataURL('image/jpeg');
        status.textContent = 'Processing...';
        const r = await fetch('/api/method/face_attendance_app.api.mark_attendance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image: dataUrl })
        });
        const res = await r.json();
        if (res.message && res.message.status === 'success') {
            status.textContent = 'Welcome ' + res.message.employee;
        } else {
            status.textContent = 'Face not recognized';
        }
    });
})();
