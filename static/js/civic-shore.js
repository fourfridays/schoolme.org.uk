(() => {
    "use strict";

    const sections = document.querySelectorAll(".block-starfish");
    if (!sections.length) return;

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    class CivicOcean {
        constructor(section) {
            this.section = section;
            this.canvas = document.createElement("canvas");
            this.canvas.className = "civic-ocean-canvas";
            this.canvas.setAttribute("aria-hidden", "true");
            this.canvas.setAttribute("role", "presentation");
            this.ctx = this.canvas.getContext("2d", { alpha: false });
            this.frame = 0;
            this.visible = true;
            this.motionReduced = reduceMotion.matches;
            this.lastTime = 0;
            this.time = 0;
            this.foam = this.createFoam(54);
            section.prepend(this.canvas);

            this.resize = this.resize.bind(this);
            this.tick = this.tick.bind(this);
            this.onMotionChange = this.onMotionChange.bind(this);
            this.resizeObserver = new ResizeObserver(this.resize);
            this.resizeObserver.observe(section);

            this.intersectionObserver = new IntersectionObserver((entries) => {
                this.visible = entries[0].isIntersecting;
                if (this.visible && !this.motionReduced && !this.frame) {
                    this.frame = requestAnimationFrame(this.tick);
                }
            }, { rootMargin: "120px" });
            this.intersectionObserver.observe(section);

            if (reduceMotion.addEventListener) {
                reduceMotion.addEventListener("change", this.onMotionChange);
            } else {
                reduceMotion.addListener(this.onMotionChange);
            }

            this.resize();
        }

        createFoam(count) {
            return Array.from({ length: count }, (_, index) => {
                const seed = (index * 9301 + 49297) % 233280;
                return {
                    x: (seed / 233280),
                    band: index % 4,
                    size: 0.8 + ((index * 17) % 19) / 10,
                    speed: 0.55 + ((index * 29) % 31) / 40,
                    phase: ((index * 47) % 100) / 100 * Math.PI * 2
                };
            });
        }

        onMotionChange(event) {
            this.motionReduced = event.matches;
            if (this.motionReduced) {
                cancelAnimationFrame(this.frame);
                this.frame = 0;
                this.time = 2.4;
                this.draw();
            } else if (this.visible && !this.frame) {
                this.lastTime = performance.now();
                this.frame = requestAnimationFrame(this.tick);
            }
        }

        resize() {
            const rect = this.section.getBoundingClientRect();
            const ratio = Math.min(window.devicePixelRatio || 1, 1.75);
            this.width = Math.max(1, rect.width);
            this.height = Math.max(1, rect.height);
            this.canvas.width = Math.round(this.width * ratio);
            this.canvas.height = Math.round(this.height * ratio);
            this.canvas.style.width = `${this.width}px`;
            this.canvas.style.height = `${this.height}px`;
            this.ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
            this.draw();
            if (!this.motionReduced && this.visible && !this.frame) {
                this.lastTime = performance.now();
                this.frame = requestAnimationFrame(this.tick);
            }
        }

        tick(now) {
            this.frame = 0;
            if (!this.visible || this.motionReduced) return;
            const delta = Math.min((now - (this.lastTime || now)) / 1000, 0.04);
            this.lastTime = now;
            this.time += delta;
            this.draw();
            this.frame = requestAnimationFrame(this.tick);
        }

        waveY(x, baseline, amplitude, frequency, speed, phase = 0) {
            const normalizedX = x / this.width;
            return baseline
                + Math.sin(normalizedX * frequency * Math.PI * 2 + this.time * speed + phase) * amplitude
                + Math.sin(normalizedX * (frequency * 1.83) * Math.PI * 2 - this.time * speed * 0.57 + phase * 1.4) * amplitude * 0.32;
        }

        drawSky(horizon) {
            const { ctx, width, height } = this;
            const sky = ctx.createLinearGradient(0, 0, 0, horizon);
            sky.addColorStop(0, "#8ac9f2");
            sky.addColorStop(0.58, "#d8eef9");
            sky.addColorStop(1, "#f8fcff");
            ctx.fillStyle = sky;
            ctx.fillRect(0, 0, width, height);

            const lightX = width * 0.78;
            const lightY = horizon * 0.34;
            const glow = ctx.createRadialGradient(lightX, lightY, 4, lightX, lightY, Math.max(width, height) * 0.36);
            glow.addColorStop(0, "rgba(255,255,255,.84)");
            glow.addColorStop(0.16, "rgba(255,238,178,.42)");
            glow.addColorStop(1, "rgba(255,255,255,0)");
            ctx.fillStyle = glow;
            ctx.fillRect(0, 0, width, horizon);

            ctx.fillStyle = "rgba(255,255,255,.75)";
            for (let i = 0; i < 5; i += 1) {
                const x = width * (0.09 + i * 0.19) + Math.sin(this.time * 0.035 + i) * 8;
                const y = horizon * (0.16 + (i % 3) * 0.13);
                const cloudWidth = width * (0.045 + (i % 2) * 0.018);
                ctx.beginPath();
                ctx.ellipse(x, y, cloudWidth, 5 + i % 3, 0, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        drawOceanBase(horizon) {
            const { ctx, width, height } = this;
            const sea = ctx.createLinearGradient(0, horizon, 0, height);
            sea.addColorStop(0, "#168bc1");
            sea.addColorStop(0.18, "#0876ac");
            sea.addColorStop(0.54, "#07538d");
            sea.addColorStop(1, "#042c62");
            ctx.fillStyle = sea;
            ctx.fillRect(0, horizon - 2, width, height - horizon + 2);

            const reflection = ctx.createLinearGradient(width * 0.54, 0, width * 0.9, 0);
            reflection.addColorStop(0, "rgba(189,239,255,0)");
            reflection.addColorStop(0.48, "rgba(189,239,255,.18)");
            reflection.addColorStop(0.58, "rgba(255,248,206,.42)");
            reflection.addColorStop(0.7, "rgba(189,239,255,.08)");
            reflection.addColorStop(1, "rgba(189,239,255,0)");
            ctx.fillStyle = reflection;
            ctx.fillRect(0, horizon, width, height - horizon);
        }

        drawWaveBand(options) {
            const { ctx, width, height } = this;
            const { baseline, amplitude, frequency, speed, phase, color, foam, depth } = options;
            const step = Math.max(7, width / 130);
            ctx.beginPath();
            ctx.moveTo(0, this.waveY(0, baseline, amplitude, frequency, speed, phase));
            for (let x = step; x <= width + step; x += step) {
                ctx.lineTo(x, this.waveY(x, baseline, amplitude, frequency, speed, phase));
            }
            ctx.lineTo(width, height + 4);
            ctx.lineTo(0, height + 4);
            ctx.closePath();
            ctx.fillStyle = color;
            ctx.fill();

            if (foam) {
                ctx.beginPath();
                for (let x = 0; x <= width; x += step) {
                    const y = this.waveY(x, baseline, amplitude, frequency, speed, phase);
                    if (x === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }
                ctx.strokeStyle = foam;
                ctx.lineWidth = Math.max(1, 3.4 - depth * 0.38);
                ctx.lineCap = "round";
                ctx.stroke();
            }
        }

        drawCurrents(horizon) {
            const { ctx, width, height } = this;
            ctx.save();
            ctx.globalCompositeOperation = "screen";
            for (let i = 0; i < 9; i += 1) {
                const depth = i / 8;
                const y = horizon + (height - horizon) * (0.13 + depth * 0.78);
                const sway = Math.sin(this.time * (0.22 + depth * 0.1) + i * 1.9) * width * 0.025;
                ctx.beginPath();
                ctx.moveTo(-width * 0.08, y + sway);
                ctx.bezierCurveTo(
                    width * 0.24, y - 30 - depth * 20,
                    width * 0.62, y + 42 + sway,
                    width * 1.08, y - 12
                );
                ctx.strokeStyle = `rgba(117, 218, 238, ${0.09 - depth * 0.035})`;
                ctx.lineWidth = 2.5 + depth * 7;
                ctx.stroke();
            }
            ctx.restore();
        }

        drawCaustics(horizon) {
            const { ctx, width, height } = this;
            ctx.save();
            ctx.globalCompositeOperation = "screen";
            ctx.lineCap = "round";
            for (let row = 0; row < 6; row += 1) {
                const y = horizon + 70 + row * ((height - horizon - 90) / 6);
                const alpha = Math.max(0.025, 0.13 - row * 0.017);
                for (let col = -1; col < 11; col += 1) {
                    const cell = width / 9;
                    const x = col * cell + ((this.time * (9 + row * 1.5)) % cell);
                    const offset = Math.sin(this.time * 0.7 + col * 1.3 + row) * cell * 0.18;
                    ctx.beginPath();
                    ctx.moveTo(x + offset, y);
                    ctx.quadraticCurveTo(x + cell * .32, y - 14 - row * 2, x + cell * .65 + offset, y + 4);
                    ctx.strokeStyle = `rgba(180, 244, 246, ${alpha})`;
                    ctx.lineWidth = 1.3 + row * .32;
                    ctx.stroke();
                }
            }
            ctx.restore();
        }

        drawFoam(horizon) {
            const { ctx, width, height } = this;
            for (const particle of this.foam) {
                const bandY = horizon + 22 + particle.band * ((height - horizon) * 0.11);
                const x = ((particle.x * width + this.time * 18 * particle.speed) % (width + 40)) - 20;
                const y = this.waveY(x, bandY, 5 + particle.band * 2.5, 2 + particle.band * .28, .85, particle.phase);
                const shimmer = 0.45 + Math.sin(this.time * 1.8 + particle.phase) * 0.25;
                ctx.fillStyle = `rgba(237, 252, 255, ${Math.max(.12, shimmer)})`;
                ctx.beginPath();
                ctx.ellipse(x, y, particle.size * (1.8 + particle.band * .25), particle.size * .55, -.18, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        draw() {
            if (!this.ctx || !this.width || !this.height) return;
            const horizon = this.height * 0.38;
            this.drawSky(horizon);
            this.drawOceanBase(horizon);

            const bands = [
                { baseline: horizon + 2, amplitude: 4, frequency: 2.2, speed: .78, phase: .8, color: "rgba(20,137,185,.72)", foam: "rgba(246,253,255,.86)", depth: 0 },
                { baseline: horizon + 34, amplitude: 8, frequency: 1.8, speed: .66, phase: 2.1, color: "rgba(8,111,164,.54)", foam: "rgba(205,244,250,.56)", depth: 1 },
                { baseline: horizon + this.height * .12, amplitude: 13, frequency: 1.43, speed: .57, phase: 4.3, color: "rgba(5,86,142,.42)", foam: "rgba(176,230,239,.42)", depth: 2 },
                { baseline: horizon + this.height * .25, amplitude: 20, frequency: 1.08, speed: .43, phase: 1.4, color: "rgba(4,64,117,.35)", foam: "rgba(136,208,224,.3)", depth: 3 }
            ];
            bands.forEach((band) => this.drawWaveBand(band));
            this.drawCurrents(horizon);
            this.drawCaustics(horizon);
            this.drawFoam(horizon);
        }
    }

    sections.forEach((section) => new CivicOcean(section));
})();
