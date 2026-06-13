const API_BASE = window.location.origin;

let editingIndex = null;
let currentUsername = null;

// ===== Login =====

function normalizeBackendText(text) {
    let normalized = text.trim();
    if (normalized.startsWith('"') && normalized.endsWith('"')) {
        normalized = normalized.slice(1, -1);
    }
    return normalized;
}

async function login(username, password) {
    const params = new URLSearchParams({ Username: username, Password: password });
    const res = await fetch(`${API_BASE}/login?${params}`, { method: 'GET' });
    if (!res.ok) throw new Error('Gagal menghubungi server');
    const text = normalizeBackendText(await res.text());
    console.log('Login response:', text);
    return text;
}

async function signup(username, password, namaLengkap, umur, citaCita) {
    const params = new URLSearchParams({ 
        Username: username, 
        Password: password,
        Nama_Lengkap: namaLengkap,
        Umur: umur,
        Cita_cita: citaCita
    });
    const res = await fetch(`${API_BASE}/Sign%20Up?${params}`, { method: 'POST' });
    if (!res.ok) throw new Error('Gagal menghubungi server');
    return res.text();
}

async function hapusAkun(username) {
    const params = new URLSearchParams({ Username: username });
    const res = await fetch(`${API_BASE}/Hapus%20Akun?${params}`, { method: 'DELETE' });
    if (!res.ok) throw new Error('Gagal menghubungi server');
    return res.text();
}

// Toggle Login/Signup
document.getElementById('toggle-signup').addEventListener('click', () => {
    document.getElementById('login-form-container').style.display = 'none';
    document.getElementById('signup-form-container').style.display = 'block';
});

document.getElementById('toggle-login').addEventListener('click', () => {
    document.getElementById('signup-form-container').style.display = 'none';
    document.getElementById('login-form-container').style.display = 'block';
});

// Signup Form Handler
document.getElementById('signup-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('signup-username').value.trim();
    const password = document.getElementById('signup-password').value.trim();
    const namaLengkap = document.getElementById('signup-nama-lengkap').value.trim();
    const umur = document.getElementById('signup-umur').value.trim();
    const citaCita = document.getElementById('signup-cita-cita').value.trim();
    const errorEl = document.getElementById('signup-error');

    if (!username || !password || !namaLengkap || !umur || !citaCita) {
        errorEl.textContent = 'Semua field harus diisi!';
        errorEl.style.display = 'block';
        return;
    }

    try {
        const result = await signup(username, password, namaLengkap, umur, citaCita);
        if (result.includes('berhasil')) {
            errorEl.style.display = 'none';
            alert('Pendaftaran berhasil! Silakan login.');
            document.getElementById('signup-form').reset();
            document.getElementById('signup-form-container').style.display = 'none';
            document.getElementById('login-form-container').style.display = 'block';
        } else {
            errorEl.textContent = 'Gagal mendaftar!';
            errorEl.style.display = 'block';
        }
    } catch (err) {
        errorEl.textContent = 'Gagal menghubungi server.';
        errorEl.style.display = 'block';
    }
});

// Login Form Handler
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('login-username').value.trim();
    const password = document.getElementById('login-password').value.trim();
    const errorEl = document.getElementById('login-error');

    if (!username || !password) return;

    try {
        const result = await login(username, password);
        if (result === 'Login successful') {
            currentUsername = username;
            document.getElementById('login-screen').style.display = 'none';
            document.getElementById('app-screen').style.display = 'block';
            renderDiaries();
        } else {
            errorEl.textContent = 'Username atau password salah!';
            errorEl.style.display = 'block';
        }
    } catch (err) {
        errorEl.textContent = 'Gagal menghubungi server.';
        errorEl.style.display = 'block';
    }
});

document.getElementById('btn-logout').addEventListener('click', () => {
    document.getElementById('app-screen').style.display = 'none';
    document.getElementById('login-screen').style.display = 'flex';
    document.getElementById('login-form').reset();
    document.getElementById('login-error').style.display = 'none';
    currentUsername = null;
});

document.getElementById('btn-delete-account').addEventListener('click', async () => {
    if (!currentUsername) return;
    
    const confirmed = confirm('Apakah Anda yakin ingin menghapus akun? Tindakan ini tidak dapat dibatalkan dan semua data Anda akan hilang.');
    if (!confirmed) return;
    
    try {
        const result = await hapusAkun(currentUsername);
        alert('Akun berhasil dihapus. Anda akan dialihkan ke halaman login.');
        document.getElementById('app-screen').style.display = 'none';
        document.getElementById('login-screen').style.display = 'flex';
        document.getElementById('login-form').reset();
        document.getElementById('login-error').style.display = 'none';
        currentUsername = null;
    } catch (err) {
        alert('Gagal menghapus akun: ' + err.message);
    }
});

// ===== Utility Functions =====

function formatDate(dateStr) {
    // Handle both "DD/MM/YYYY" and "YYYY-MM-DD" formats
    if (dateStr.includes('/')) {
        return dateStr;
    }
    const [y, m, d] = dateStr.split('-');
    return `${d}/${m}/${y}`;
}

function parseDateForInput(dateStr) {
    // Convert "DD/MM/YYYY" to "YYYY-MM-DD" for input[type=date]
    if (dateStr.includes('/')) {
        const [d, m, y] = dateStr.split('/');
        return `${y}-${m.padStart(2, '0')}-${d.padStart(2, '0')}`;
    }
    return dateStr;
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast ${type}`;
    toast.style.display = 'block';
    setTimeout(() => {
        toast.style.display = 'none';
    }, 2500);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ===== Parse diary string from backend =====
function parseDiaryString(str) {
    // Backend stores dicts as Python repr strings like: {'Tanggalnya': '...', ...}
    // Try JSON first (if backend returns parsed JSON)
    if (typeof str === 'object' && str !== null) {
        return str;
    }
    try {
        // Replace Python single quotes with double quotes for JSON
        const jsonStr = str
            .replace(/'/g, '"');
        return JSON.parse(jsonStr);
    } catch {
        return null;
    }
}

// ===== API Calls =====

async function fetchDiaries() {
    try {
        const res = await fetch(`${API_BASE}/Diary`);
        const data = await res.json();
        return data;
    } catch (err) {
        showToast('Gagal memuat diary', 'error');
        return [];
    }
}

async function createDiary(tanggal, judul, isi) {
    const params = new URLSearchParams({ Tanggal: tanggal, Judul: judul, Isi: isi });
    const res = await fetch(`${API_BASE}/Diary?${params}`, { method: 'POST' });
    if (!res.ok) throw new Error('Gagal membuat diary');
    return res.json();
}

async function deleteDiary(urutan) {
    const params = new URLSearchParams({ Urutan: urutan.toString() });
    const res = await fetch(`${API_BASE}/Diary?${params}`, { method: 'DELETE' });
    if (!res.ok) throw new Error('Gagal menghapus diary');
    return res.json();
}

async function updateDiary(urutan, pilihan, mengganti) {
    const params = new URLSearchParams({
        Urutan: urutan.toString(),
        Pilihan: pilihan,
        Mengganti: mengganti
    });
    const res = await fetch(`${API_BASE}/Diary?${params}`, { method: 'PUT' });
    if (!res.ok) throw new Error('Gagal mengubah diary');
    return res.json();
}

// Store parsed diary data for edit access
let diaryData = [];

// ===== Render Diary List =====

async function renderDiaries() {
    const listEl = document.getElementById('diary-list');
    const emptyEl = document.getElementById('empty-state');

    const diaries = await fetchDiaries();

    // Filter out empty strings
    const validDiaries = diaries.filter(d => d && d.trim && d.trim() !== '');

    if (validDiaries.length === 0) {
        listEl.innerHTML = '';
        diaryData = [];
        emptyEl.style.display = 'block';
        return;
    }

    emptyEl.style.display = 'none';
    listEl.innerHTML = '';
    diaryData = [];

    validDiaries.forEach((item, idx) => {
        const diary = parseDiaryString(item);
        if (!diary) return;

        const tanggal = diary.Tanggalnya || '-';
        const judul = diary.Judulnya || '-';
        const isi = diary.Isi || diary.Isinya || '-';
        const urutan = idx + 1;

        // Store raw data for edit
        diaryData.push({ urutan, tanggal, judul, isi });

        const entry = document.createElement('div');
        entry.className = 'diary-entry';

        entry.innerHTML = `
            <div class="diary-header">
                <div class="diary-meta">
                    <span class="diary-number">#${urutan}</span>
                    <div class="diary-date">📅 ${escapeHtml(tanggal)}</div>
                    <div class="diary-title">${escapeHtml(judul)}</div>
                </div>
                <div class="diary-actions">
                    <button class="btn btn-secondary btn-sm btn-edit" data-index="${idx}">✏️ Edit</button>
                    <button class="btn btn-danger btn-sm" onclick="openDeleteModal(${urutan})">🗑️</button>
                </div>
            </div>
            <div class="diary-content">${escapeHtml(isi)}</div>
        `;

        // Attach edit handler via addEventListener (safe from escaping issues)
        entry.querySelector('.btn-edit').addEventListener('click', () => {
            startEdit(urutan, tanggal, judul, isi);
        });

        listEl.appendChild(entry);
    });
}

// ===== Form Handling =====

document.getElementById('diary-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const tanggalInput = document.getElementById('tanggal').value;
    const judul = document.getElementById('judul').value.trim();
    const isi = document.getElementById('isi').value.trim();

    if (!tanggalInput || !judul || !isi) return;

    const tanggal = formatDate(tanggalInput);

    try {
        if (editingIndex !== null) {
            // Update mode: send changes for each field
            const original = window._editOriginal || {};
            if (original.tanggal !== tanggal) {
                await updateDiary(editingIndex, 'Tanggal', tanggal);
            }
            if (original.judul !== judul) {
                await updateDiary(editingIndex, 'Judul', judul);
            }
            if (original.isi !== isi) {
                await updateDiary(editingIndex, 'Isi', isi);
            }
            showToast('Diary berhasil diubah!');
            cancelEdit();
        } else {
            await createDiary(tanggal, judul, isi);
            showToast('Diary berhasil disimpan!');
        }

        document.getElementById('diary-form').reset();
        await renderDiaries();
    } catch (err) {
        showToast(err.message, 'error');
    }
});

// ===== Edit Mode =====

function startEdit(urutan, tanggal, judul, isi) {
    editingIndex = urutan;
    window._editOriginal = { tanggal, judul, isi };

    document.getElementById('tanggal').value = parseDateForInput(tanggal);
    document.getElementById('judul').value = judul;
    document.getElementById('isi').value = isi;

    document.getElementById('form-title').textContent = '✏️ Edit Diary #' + urutan;
    document.getElementById('btn-text').textContent = 'Simpan Perubahan';
    document.getElementById('btn-cancel').style.display = 'inline-block';

    // Scroll to form
    document.querySelector('.form-card').scrollIntoView({ behavior: 'smooth' });
}

function cancelEdit() {
    editingIndex = null;
    window._editOriginal = null;

    document.getElementById('diary-form').reset();
    document.getElementById('form-title').textContent = '✏️ Tulis Diary Baru';
    document.getElementById('btn-text').textContent = 'Simpan Diary';
    document.getElementById('btn-cancel').style.display = 'none';
}

// ===== Delete Modal =====

let deleteTarget = null;

function openDeleteModal(urutan) {
    deleteTarget = urutan;
    document.getElementById('delete-modal').style.display = 'flex';
}

function closeDeleteModal() {
    deleteTarget = null;
    document.getElementById('delete-modal').style.display = 'none';
}

document.getElementById('btn-confirm-delete').addEventListener('click', async () => {
    if (deleteTarget === null) return;
    try {
        await deleteDiary(deleteTarget);
        showToast('Diary berhasil dihapus!');
        closeDeleteModal();
        await renderDiaries();
    } catch (err) {
        showToast(err.message, 'error');
        closeDeleteModal();
    }
});

// Close modal on overlay click
document.getElementById('delete-modal').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) closeDeleteModal();
});

// ===== Set default date to today =====
document.getElementById('tanggal').valueAsDate = new Date();
