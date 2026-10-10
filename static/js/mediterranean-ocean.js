(() => {
  "use strict";

  const scenes = document.querySelectorAll("[data-ocean-scene]");
  if (!scenes.length) return;

  const TAU = Math.PI * 2;
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  class DawnOcean {
    constructor(root) {
      this.root = root;
      this.canvas = root.querySelector("canvas");
      this.ctx = this.canvas && this.canvas.getContext("2d", { alpha: false });
      this.frame = 0;
      this.width = 0;
      this.height = 0;
      this.dpr = 1;
      this.running = false;
      this.visible = true;
      this.seed = 1978;
      this.particles = Array.from({ length: 38 }, (_, index) => ({
        x: this.random(),
        y: .48 + this.random() * .42,
        radius: .45 + this.random() * 1.5,
        speed: .12 + this.random() * .28,
        phase: index * 1.73
      }));

      if (!this.ctx) return;
      this.resize = this.resize.bind(this);
      this.tick = this.tick.bind(this);
      this.handlePreference = this.handlePreference.bind(this);
      this.resizeObserver = "ResizeObserver" in window ? new ResizeObserver(this.resize) : null;
      this.intersectionObserver = "IntersectionObserver" in window
        ? new IntersectionObserver(([entry]) => {
            this.visible = entry.isIntersecting;
            if (this.visible) this.start();
            else this.stop();
          }, { rootMargin: "160px" })
        : null;

      this.resizeObserver?.observe(root);
      this.intersectionObserver?.observe(root);
      window.addEventListener("resize", this.resize, { passive: true });
      document.addEventListener("visibilitychange", () => {
        this.visible = !document.hidden;
        if (this.visible) this.start();
        else this.stop();
      });
      reducedMotion.addEventListener?.("change", this.handlePreference);
      this.resize();
      this.start();
    }

    random() {
      this.seed = (this.seed * 16807) % 2147483647;
      return (this.seed - 1) / 2147483646;
    }

    resize() {
      if (!this.ctx) return;
      const bounds = this.root.getBoundingClientRect();
      const width = Math.max(1, Math.round(bounds.width));
      const height = Math.max(1, Math.round(bounds.height));
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      if (width === this.width && height === this.height && dpr === this.dpr) return;
      this.width = width;
      this.height = height;
      this.dpr = dpr;
      this.canvas.width = Math.round(width * dpr);
      this.canvas.height = Math.round(height * dpr);
      this.canvas.style.width = `${width}px`;
      this.canvas.style.height = `${height}px`;
      this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      this.draw(reducedMotion.matches ? 24 : performance.now() * .001);
    }

    handlePreference() {
      if (reducedMotion.matches) {
        this.stop();
        this.draw(24);
      } else {
        this.start();
      }
    }

    start() {
      if (this.running || !this.visible || reducedMotion.matches || !this.ctx) return;
      this.running = true;
      this.frame = requestAnimationFrame(this.tick);
    }

    stop() {
      this.running = false;
      cancelAnimationFrame(this.frame);
    }

    tick(timestamp) {
      if (!this.running) return;
      this.draw(timestamp * .001);
      this.frame = requestAnimationFrame(this.tick);
    }

    waveY(x, base, amplitude, frequency, time, speed, phase) {
      return base
        + Math.sin(x * frequency + time * speed + phase) * amplitude
        + Math.sin(x * frequency * 2.17 - time * speed * .63 + phase * 1.8) * amplitude * .34
        + Math.cos(x * frequency * .49 + time * speed * .31) * amplitude * .2;
    }

    drawSky(ctx, w, h, horizon) {
      const sky = ctx.createLinearGradient(0, 0, 0, horizon + 30);
      sky.addColorStop(0, "#65b9d4");
      sky.addColorStop(.48, "#9cd5dd");
      sky.addColorStop(.78, "#f7c58d");
      sky.addColorStop(1, "#f09a72");
      ctx.fillStyle = sky;
      ctx.fillRect(0, 0, w, horizon + 40);

      const sunX = w * .77;
      const sunY = horizon * .48;
      const glow = ctx.createRadialGradient(sunX, sunY, 2, sunX, sunY, Math.min(w, h) * .25);
      glow.addColorStop(0, "rgba(255,249,202,.95)");
      glow.addColorStop(.13, "rgba(255,215,116,.48)");
      glow.addColorStop(.55, "rgba(255,190,105,.12)");
      glow.addColorStop(1, "rgba(255,190,105,0)");
      ctx.fillStyle = glow;
      ctx.fillRect(0, 0, w, horizon);
      ctx.beginPath();
      ctx.arc(sunX, sunY, Math.max(24, Math.min(w, h) * .045), 0, TAU);
      ctx.fillStyle = "#fff3bd";
      ctx.fill();

      const haze = ctx.createLinearGradient(0, horizon - 90, 0, horizon + 18);
      haze.addColorStop(0, "rgba(255,255,255,0)");
      haze.addColorStop(1, "rgba(255,235,204,.38)");
      ctx.fillStyle = haze;
      ctx.fillRect(0, horizon - 90, w, 110);

      ctx.fillStyle = "rgba(15,74,91,.32)";
      ctx.beginPath();
      ctx.moveTo(0, horizon + 2);
      ctx.lineTo(w * .12, horizon - 12);
      ctx.lineTo(w * .19, horizon - 5);
      ctx.lineTo(w * .29, horizon - 17);
      ctx.lineTo(w * .38, horizon + 2);
      ctx.closePath();
      ctx.fill();
    }

    drawSeaBase(ctx, w, h, horizon) {
      const sea = ctx.createLinearGradient(0, horizon, 0, h);
      sea.addColorStop(0, "#298ba7");
      sea.addColorStop(.34, "#087899");
      sea.addColorStop(.72, "#075875");
      sea.addColorStop(1, "#043d58");
      ctx.fillStyle = sea;
      ctx.fillRect(0, horizon, w, h - horizon);
    }

    drawReflection(ctx, w, h, horizon, time) {
      const sunX = w * .77;
      ctx.save();
      ctx.globalCompositeOperation = "screen";
      for (let row = 0; row < 28; row += 1) {
        const progress = row / 27;
        const y = horizon + 10 + progress * (h - horizon - 22);
        const spread = 12 + progress * w * .17;
        const count = 2 + Math.floor(progress * 4);
        for (let piece = 0; piece < count; piece += 1) {
          const jitter = Math.sin(row * 3.1 + piece * 5.3 + time * 1.7) * spread;
          const length = (10 + progress * 46) * (.55 + .45 * Math.sin(piece + row * 2.7) ** 2);
          ctx.beginPath();
          ctx.moveTo(sunX + jitter - length / 2, y);
          ctx.quadraticCurveTo(sunX + jitter, y - 1.8, sunX + jitter + length / 2, y);
          ctx.strokeStyle = `rgba(255,220,145,${.1 + (1 - progress) * .2})`;
          ctx.lineWidth = .7 + progress * 1.7;
          ctx.stroke();
        }
      }
      ctx.restore();
    }

    drawWaveLayer(ctx, w, h, time, layer) {
      const depth = layer / 6;
      const base = h * (.52 + depth * .082);
      const amplitude = 2.3 + depth * 11;
      const frequency = .018 - depth * .009;
      const speed = .34 + depth * .42;
      const step = Math.max(5, Math.round(w / 180));
      const palette = [
        "rgba(55,157,178,.62)", "rgba(30,139,164,.68)", "rgba(19,121,150,.76)",
        "rgba(11,103,133,.82)", "rgba(8,86,117,.88)", "rgba(5,70,99,.94)", "#043d58"
      ];

      ctx.beginPath();
      ctx.moveTo(0, h);
      for (let x = 0; x <= w + step; x += step) {
        ctx.lineTo(x, this.waveY(x, base, amplitude, frequency, time, speed, layer * .9));
      }
      ctx.lineTo(w, h);
      ctx.closePath();
      ctx.fillStyle = palette[layer];
      ctx.fill();

      ctx.beginPath();
      for (let x = 0; x <= w + step; x += step) {
        const y = this.waveY(x, base, amplitude, frequency, time, speed, layer * .9);
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.strokeStyle = `rgba(194,238,238,${.18 + depth * .12})`;
      ctx.lineWidth = .7 + depth * 1.15;
      ctx.stroke();

      if (layer > 2) {
        ctx.save();
        ctx.setLineDash([18 + layer * 3, 28 + layer * 5]);
        ctx.lineDashOffset = -time * (6 + layer * 2);
        ctx.beginPath();
        for (let x = -20; x <= w + 20; x += step) {
          const y = this.waveY(x, base + 4 + depth * 5, amplitude * .68, frequency * 1.12, time, speed, layer * 1.3);
          if (x === -20) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.strokeStyle = `rgba(225,249,246,${.08 + depth * .13})`;
        ctx.lineWidth = 1 + depth * 1.8;
        ctx.stroke();
        ctx.restore();
      }
    }

    drawParticles(ctx, w, h, time) {
      ctx.save();
      ctx.globalCompositeOperation = "screen";
      for (const particle of this.particles) {
        const drift = (time * particle.speed + particle.phase) % 1.25;
        const x = ((particle.x + drift) % 1.25 - .1) * w;
        const y = particle.y * h + Math.sin(time * .8 + particle.phase) * 9;
        const alpha = .12 + .18 * Math.sin(time + particle.phase) ** 2;
        ctx.beginPath();
        ctx.arc(x, y, particle.radius, 0, TAU);
        ctx.fillStyle = `rgba(223,249,245,${alpha})`;
        ctx.fill();
      }
      ctx.restore();
    }

    draw(time) {
      const { ctx, width: w, height: h } = this;
      if (!ctx || !w || !h) return;
      ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
      const horizon = h * .49;
      this.drawSky(ctx, w, h, horizon);
      this.drawSeaBase(ctx, w, h, horizon);
      this.drawReflection(ctx, w, h, horizon, time);
      for (let layer = 0; layer < 7; layer += 1) this.drawWaveLayer(ctx, w, h, time, layer);
      this.drawParticles(ctx, w, h, time);
    }
  }

  scenes.forEach((scene) => new DawnOcean(scene));
})();
