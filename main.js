document.addEventListener('DOMContentLoaded', () => {
    populateTrangSelect();
});

const problemsMapping = {
    1: [
        'cac-phep-tinh-co-ban',
        'tam-giac-phai-khong',
        'hoa-don-tien-dien',
        'phuong-trinh-bac-hai-2',
        'so-chinh-phuong-trong-doan-2',
    ],
    2: [
        'tong-lap-phuong',
        'many-numbers',
        'Fibonacci-1',
        '[HSG-KC-Dong-Nai-24-25]-Chia-Sticker',
    ],
};

function populateTrangSelect() {
    const trangSelect = document.getElementById('trangSelect');
    const numberOfTrang = Object.keys(problemsMapping).length;
    for (let i = 1; i <= numberOfTrang; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.text = `Trang ${i}`;
        trangSelect.appendChild(option);
    }
    updateProblems();
}

function updateProblems() {
    const problemSelect = document.getElementById('problemSelect');
    problemSelect.innerHTML = '';
    const trang = document.getElementById('trangSelect').value;
    const problems = problemsMapping[trang] || [];
    problems.forEach(problem => {
        const option = document.createElement('option');
        option.value = `trang${trang}/${problem}.py`;
        option.text = problem;
        problemSelect.appendChild(option);
    });
    loadCode();
}

function loadCode() {
    const codeDisplay = document.getElementById('codeDisplay');
    const problemSelect = document.getElementById('problemSelect');
    const filePath = `resources/${problemSelect.value}`;
    
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            codeDisplay.textContent = data;
            hljs.highlightElement(codeDisplay);  // Áp dụng Highlight.js
        })
        .catch(error => {
            console.error('Error loading code:', error);
        });
}

function copyCode() {
    const codeDisplay = document.getElementById('codeDisplay');
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = codeDisplay.textContent;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
    document.getElementById('notification').classList.remove('hidden');
    setTimeout(() => {
        document.getElementById('notification').classList.add('hidden');
    }, 2000);
}
