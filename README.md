# ComfyUI-Orakul-3K-Resolution

**A node of 3K+ precise presets for ComfyUI — no math, no glitches**
**Exact 3K+ presets for ComfyUI - no math, no artifacts**

>Found experimentally. Tested in 10 steps..
>Discovered experimentally. Verified at 10 steps.

*Protocol Oracle-60 · Orakul Studio · Chernihiv, Ukraine 🇺🇦*

---

## Why Presets, Not Math

The previous version of the node calculated resolution mathematically—the same area for all formats. This caused glitches: with vertical formats, the long side tended to values ​​​​outside the Flux2 comfort zone, and the model began to break.
*The previous version calculated resolution mathematically — equal area for all formats. This caused artifacts: vertical formats pushed the long side beyond Flux2's comfortable generation zone, causing the model to break.*

**Solution:** Experimental selection of presets at **10 steps**.

Every value tested — the model generates stably, without artifacts, without doubles.

*Solution: Experimental preset selection at **10 steps**.

Every value tested — the model generates stably, no artifacts, no doubles.*

---

## Preset Table

| Format | Width | Height | Use |
|----------------|--------------|----------------|-----------------|
| `1:1 - 3k` | 3072 | 3072 | Square |
| `1:1 - 2K` | 2752 | 2752 | Reliable square |
| `3:2` | 3072 | 2048 | Landscape |
| `2:3` | 2048 | 3072 | Portrait |
| `4:3` | 3072 | 2304 | Wide |
| `3:4` | 2304 | 3072 | Tall |
| `16:9` | 3072 | 1712 | Cinematic |
| `9:16` | 1712 | 3072 | Phone |
| `21:9` | 3072 | 1312 | Ultrawide |
| `9:21` | 1312 | 3072 | Supertall |
| `2:1` | 3072 | 1536 | Panorama |
| 1:2 | 1536 | 3072 | Banner |
| 5:4 | 3072 | 2464 | Near Square |
| 4:5 | 2464 | 3072 | Social Portrait |

**All values ​​are multiples of 16. Tested on Flux2-dev.**
*All values ​​are divisible by 16. Tested on Flux2-dev.*

---

## Results

**3K square (3072×3072) at 10 steps:**
→ Generation time: **~3.5 minutes**
→ File size: ~7.3 MB PNG
→ At 800% zoom: armor fabric, finger pores — no artifacts

*3K square (3072×3072) at 10 steps:*
*→ Generation time: ~3.5 minutes*
*→ At 800% zoom: armor fabric, finger pores — zero artifacts*

---

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/OrakulStudio/ComfyUI-Orakul-3K-Resolution
```

Restart ComfyUI. Node: Category **`Oracle`**, Name **`🎞️⚙️Orakul3KResolution`**

---

## Connection

```
Orakul3KResolution
├── width → Empty Latent Image (width)
└── height → Empty Latent Image (height)
```

**Console during generation:**
```
🛠️⚙️ ORAKUL STUDIO 🛠️⚙️
🛠️⚙️ ORAKUL 3K MONOLITH: 3072x3072 🛠️⚙️
🛠️⚙️ ORAKUL STUDIO 🛠️⚙️
```

---

## Part of the Orakul Ecosystem / Part of Orakul Ecosystem

| Node / Node | Description / Description |
|------------|---------------------|
| 🎞️ **ComfyUI-Orakul-3K-Resolution** | This node / This node |
| 💾 [ComfyUI-Orakul-SVP](https://github.com/OrakulStudio/ComfyUI-Orakul-SVP) | PNG + TIFF 16-bit + EXR 32-bit |
| ⚡ [Viking Engine](https://github.com/OrakulStudio/ai-toolkit-Ostris-bonememory) | LoRA training rank 512-1280 |

---

## License / License

MIT

---

*🛠️⚙️ ORAKUL STUDIO 🛠️⚙️*
*Chernihiv, Ukraine 🇺🇦 · 2026*
