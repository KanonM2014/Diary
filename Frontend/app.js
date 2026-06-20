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
window.addEventListener('DOMContentLoaded', () => {
    console.log('Frontend script loaded and DOM ready');

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
        console.log('Attempt login for:', username);
        const result = await login(username, password);
        console.log('Server login response:', result);

        // Accept any response that contains "success" (case-insensitive)
        if (typeof result === 'string' && result.toLowerCase().includes('success')) {
            currentUsername = username;
            document.getElementById('login-screen').style.display = 'none';
            document.getElementById('app-screen').style.display = 'block';
            renderDiaries();
        } else {
            // Show server response to help debugging; fallback to generic message
            errorEl.textContent = result && result.length ? result : 'Username atau password salah!';
            errorEl.style.display = 'block';
        }
    } catch (err) {
        console.error('Login error:', err);
        errorEl.textContent = 'Gagal menghubungi server.' + (err && err.message ? ' (' + err.message + ')' : '');
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

document.getElementById('btn-update-profile').addEventListener('click', () => {
    document.getElementById('update-profile-error').style.display = 'none';
    const card = document.getElementById('update-profile-card');
    card.style.display = 'block';
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
});

document.getElementById('btn-change-password').addEventListener('click', () => {
    const usernameField = document.getElementById('change-password-username');
    usernameField.value = currentUsername || '';
    document.getElementById('change-password-card').style.display = 'block';
});

document.getElementById('btn-cancel-update-profile').addEventListener('click', () => {
    document.getElementById('update-profile-card').style.display = 'none';
    document.getElementById('update-profile-form').reset();
    document.getElementById('update-profile-error').style.display = 'none';
});

document.getElementById('btn-cancel-password').addEventListener('click', () => {
    document.getElementById('change-password-card').style.display = 'none';
    document.getElementById('change-password-form').reset();
    document.getElementById('change-password-error').style.display = 'none';
});

document.getElementById('update-profile-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const namaLengkap = document.getElementById('update-nama-lengkap').value.trim();
    const umur = document.getElementById('update-umur').value.trim();
    const citaCita = document.getElementById('update-cita-cita').value.trim();
    const errorEl = document.getElementById('update-profile-error');

    if (!namaLengkap || !umur || !citaCita) {
        errorEl.textContent = 'Nama lengkap, umur, dan cita-cita harus diisi.';
        errorEl.style.display = 'block';
        return;
    }

    if (!currentUsername) {
        errorEl.textContent = 'Anda harus login terlebih dahulu.';
        errorEl.style.display = 'block';
        return;
    }

    try {
        const result = await updateProfil(namaLengkap, umur, citaCita);
        showToast(result.toString(), 'success');
        document.getElementById('update-profile-card').style.display = 'none';
        document.getElementById('update-profile-form').reset();
        errorEl.style.display = 'none';
    } catch (err) {
        errorEl.textContent = err.message || 'Gagal memperbarui profil.';
        errorEl.style.display = 'block';
    }
});

document.getElementById('change-password-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('change-password-username').value.trim();
    const currentPassword = document.getElementById('current-password').value.trim();
    const newPassword = document.getElementById('new-password').value.trim();
    const errorEl = document.getElementById('change-password-error');

    if (!username || !currentPassword || !newPassword) {
        errorEl.textContent = 'Username, password lama, dan password baru harus diisi.';
        errorEl.style.display = 'block';
        return;
    }

    if (!currentUsername) {
        errorEl.textContent = 'Anda harus login terlebih dahulu.';
        errorEl.style.display = 'block';
        return;
    }

    if (username !== currentUsername) {
        errorEl.textContent = 'Username harus sama dengan akun yang sedang login.';
        errorEl.style.display = 'block';
        return;
    }

    try {
        const result = await gantiPassword(username, currentPassword, newPassword);
        if (result.toLowerCase().includes('berhasil')) {
            showToast('Password berhasil diganti!', 'success');
            document.getElementById('change-password-card').style.display = 'none';
            document.getElementById('change-password-form').reset();
            errorEl.style.display = 'none';
        } else {
            errorEl.textContent = result;
            errorEl.style.display = 'block';
        }
    } catch (err) {
        errorEl.textContent = err.message || 'Gagal mengganti password.';
        errorEl.style.display = 'block';
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
    const params = new URLSearchParams({ tanggal: tanggal, judul: judul, isi: isi });
    const res = await fetch(`${API_BASE}/Diary?${params}`, { method: 'POST' });
    const text = await res.text();
    console.log('createDiary response status:', res.status, 'body:', text);
    if (!res.ok) throw new Error(text || 'Gagal membuat diary');
    return text;
}

async function deleteDiary(urutan) {
    const params = new URLSearchParams({ Urutan: urutan.toString() });
    const res = await fetch(`${API_BASE}/Diary?${params}`, { method: 'DELETE' });
    if (!res.ok) throw new Error('Gagal menghapus diary');
    return res.json();
}

async function gantiPassword(username, passwordLama, passwordBaru) {
    const params = new URLSearchParams({
        Username: username,
        Password_Lama: passwordLama,
        Password_Baru: passwordBaru
    });
    const res = await fetch(`${API_BASE}/Ganti%20Password?${params}`, { method: 'PUT' });
    const text = await res.text();
    console.log('gantiPassword response status:', res.status, 'body:', text);
    if (!res.ok) throw new Error(text || 'Gagal mengganti password');
    return text;
}

async function updateProfil(namaLengkap, umur, citaCita) {
    if (!currentUsername) throw new Error('Anda harus login terlebih dahulu.');

    const params = new URLSearchParams({
        Username: currentUsername,
        Nama_Lengkap: namaLengkap,
        Umur: umur,
        Cita_cita: citaCita
    });
    const res = await fetch(`${API_BASE}/Update%20Profil?${params}`, { method: 'PUT' });
    const text = await res.text();
    console.log('updateProfil response status:', res.status, 'body:', text);
    if (!res.ok) throw new Error(text || 'Gagal memperbarui profil');
    return text;
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

    // Normalize list and filter empty entries (support string, array (tuple), or object)
    let validDiaries = Array.isArray(diaries) ? diaries : [];
    validDiaries = validDiaries.filter(d => {
        if (d == null) return false;
        if (typeof d === 'string') return d.trim() !== '';
        if (Array.isArray(d)) return d.length >= 4; // expect [id, Tanggal, Judul, Isi]
        if (typeof d === 'object') return Object.keys(d).length > 0;
        return true;
    });

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
        let tanggal = '-';
        let judul = '-';
        let isi = '-';
        let dbId = idx + 1; // fallback id for display if not provided by backend

        if (typeof item === 'string') {
            const parsed = parseDiaryString(item);
            if (!parsed) return;
            tanggal = parsed.Tanggalnya || parsed.Tanggal || parsed.tanggal || '-';
            judul = parsed.Judulnya || parsed.Judul || parsed.judul || '-';
            isi = parsed.Isi || parsed.Isinya || parsed.isi || '-';
        } else if (Array.isArray(item)) {
            // SQLite row tuple: [id, Tanggal, Judul, Isi]
            dbId = item[0] || dbId;
            tanggal = item[1] || '-';
            judul = item[2] || '-';
            isi = item[3] || '-';
        } else if (typeof item === 'object') {
            dbId = item.id || item.ID || item[0] || dbId;
            tanggal = item.Tanggal || item.tanggal || item.Tanggalnya || '-';
            judul = item.Judul || item.judul || item.Judulnya || '-';
            isi = item.Isi || item.isi || item.Isinya || '-';
        }

        const displayNumber = idx + 1;

        // Store raw data for edit (use dbId for update/delete)
        diaryData.push({ urutan: dbId, tanggal, judul, isi });

        const entry = document.createElement('div');
        entry.className = 'diary-entry';

        entry.innerHTML = `
            <div class="diary-header">
                <div class="diary-meta">
                    <span class="diary-number">#${displayNumber}</span>
                    <div class="diary-date">📅 ${escapeHtml(tanggal)}</div>
                    <div class="diary-title">${escapeHtml(judul)}</div>
                </div>
                <div class="diary-actions">
                    <button class="btn btn-secondary btn-sm btn-edit" data-index="${idx}">✏️ Edit</button>
                    <button class="btn btn-danger btn-sm" onclick="openDeleteModal(${dbId})">🗑️</button>
                </div>
            </div>
            <div class="diary-content">${escapeHtml(isi)}</div>
        `;

        // Attach edit handler via addEventListener (safe from escaping issues)
        entry.querySelector('.btn-edit').addEventListener('click', () => {
            startEdit(dbId, tanggal, judul, isi);
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
