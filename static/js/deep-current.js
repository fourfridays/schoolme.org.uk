/* Deep Current night-ocean canvas. No dependencies. */
(function () {
    "use strict";

    var oceans = document.querySelectorAll("[data-deep-current-ocean]");
    if (!oceans.length) {
        return;
    }

    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    function seededRandom(seed) {
        var value = seed % 2147483647;
        return function () {
            value = value * 16807 % 2147483647;
            return (value - 1) / 2147483646;
        };
    }

    function createOcean(root, index) {
        var canvas = root.querySelector("canvas.deep-current-ocean");
        var context = canvas && canvas.getContext("2d");
        if (!context) {
            return;
        }

        var width = 1;
        var height = 1;
        var scale = 1;
        var visible = true;
        var running = false;
        var frame = null;
        var start = performance.now();
        var pointer = { x: 0, y: 0, tx: 0, ty: 0 };
        var random = seededRandom(1729 + index * 97);
        var stars = [];

        for (var i = 0; i < 110; i += 1) {
            stars.push({
                x: random(),
                y: random() * 0.48,
                radius: 0.35 + random() * 1.25,
                alpha: 0.2 + random() * 0.62,
                phase: random() * Math.PI * 2,
                drift: 0.2 + random() * 0.7
            });
        }

        function resize() {
            var bounds = root.getBoundingClientRect();
            width = Math.max(1, Math.round(bounds.width));
            height = Math.max(1, Math.round(bounds.height));
            scale = Math.min(window.devicePixelRatio || 1, 2);
            canvas.width = Math.round(width * scale);
            canvas.height = Math.round(height * scale);
            canvas.style.width = width + "px";
            canvas.style.height = height + "px";
            context.setTransform(scale, 0, 0, scale, 0, 0);
            draw(reducedMotion.matches ? 4.25 : (performance.now() - start) / 1000);
        }

        function waveY(x, time, layer) {
            var amplitude = layer.amplitude * Math.min(1.35, width / 1100);
            return layer.base +
                Math.sin(x * layer.frequency + time * layer.speed + layer.phase) * amplitude +
                Math.sin(x * layer.frequency * 0.43 - time * layer.speed * 0.62 + layer.phase * 1.7) * amplitude * 0.52 +
                Math.cos(x * layer.frequency * 1.77 + time * layer.speed * 0.35) * amplitude * 0.18;
        }

        function traceWave(time, layer) {
            var path = new Path2D();
            path.moveTo(-12, waveY(-12, time, layer));
            for (var x = 0; x <= width + 16; x += 8) {
                path.lineTo(x, waveY(x, time, layer));
            }
            return path;
        }

        function drawSky(time) {
            var sky = context.createLinearGradient(0, 0, 0, height * 0.68);
            sky.addColorStop(0, "#020810");
            sky.addColorStop(0.48, "#071b29");
            sky.addColorStop(0.82, "#123a4b");
            sky.addColorStop(1, "#16495a");
            context.fillStyle = sky;
            context.fillRect(0, 0, width, height);

            var haze = context.createRadialGradient(width * 0.74, height * 0.26, 0, width * 0.74, height * 0.26, width * 0.48);
            haze.addColorStop(0, "rgba(120, 205, 220, 0.14)");
            haze.addColorStop(0.4, "rgba(70, 155, 177, 0.07)");
            haze.addColorStop(1, "rgba(10, 31, 45, 0)");
            context.fillStyle = haze;
            context.fillRect(0, 0, width, height * 0.65);

            pointer.x += (pointer.tx - pointer.x) * 0.025;
            pointer.y += (pointer.ty - pointer.y) * 0.025;
            var starShiftX = pointer.x * 8;
            var starShiftY = pointer.y * 4;

            stars.forEach(function (star) {
                var twinkle = reducedMotion.matches ? 0.82 : 0.72 + Math.sin(time * star.drift + star.phase) * 0.28;
                context.beginPath();
                context.arc(star.x * width + starShiftX, star.y * height + starShiftY, star.radius, 0, Math.PI * 2);
                context.fillStyle = "rgba(213, 244, 247, " + (star.alpha * twinkle).toFixed(3) + ")";
                context.fill();
            });
        }

        function drawMoon(time) {
            var moonX = width * 0.78 + pointer.x * 13;
            var moonY = Math.max(102, height * 0.19) + pointer.y * 6;
            var radius = Math.max(34, Math.min(68, width * 0.05));
            var glow = context.createRadialGradient(moonX, moonY, radius * 0.25, moonX, moonY, radius * 3.2);
            glow.addColorStop(0, "rgba(222, 250, 249, 0.34)");
            glow.addColorStop(0.3, "rgba(145, 224, 230, 0.14)");
            glow.addColorStop(1, "rgba(100, 198, 214, 0)");
            context.fillStyle = glow;
            context.fillRect(moonX - radius * 3.3, moonY - radius * 3.3, radius * 6.6, radius * 6.6);

            var disc = context.createRadialGradient(moonX - radius * 0.25, moonY - radius * 0.28, radius * 0.08, moonX, moonY, radius);
            disc.addColorStop(0, "#f4ffff");
            disc.addColorStop(0.7, "#d8f4f2");
            disc.addColorStop(1, "#a8d4d7");
            context.beginPath();
            context.arc(moonX, moonY, radius, 0, Math.PI * 2);
            context.fillStyle = disc;
            context.fill();

            context.save();
            context.globalAlpha = 0.12;
            context.fillStyle = "#426e78";
            [[-0.28, -0.1, 0.16], [0.24, 0.16, 0.12], [0.06, -0.32, 0.09], [-0.05, 0.34, 0.2]].forEach(function (mark) {
                context.beginPath();
                context.ellipse(moonX + radius * mark[0], moonY + radius * mark[1], radius * mark[2], radius * mark[2] * 0.62, time * 0.01, 0, Math.PI * 2);
                context.fill();
            });
            context.restore();
        }

        function drawReflection(time, horizon) {
            var center = width * 0.78 + pointer.x * 10;
            var maxY = height * 0.98;
            context.save();
            context.globalCompositeOperation = "screen";
            for (var y = horizon + 8; y < maxY; y += 7) {
                var progress = (y - horizon) / Math.max(1, maxY - horizon);
                var spread = 8 + progress * width * 0.13;
                var shimmer = Math.sin(y * 0.09 + time * 1.7) * spread * 0.34 + Math.sin(y * 0.21 - time) * 6;
                var segment = spread * (0.22 + (Math.sin(y * 0.37 + time * 2.1) + 1) * 0.16);
                var alpha = (1 - progress) * 0.18 + 0.025;
                context.strokeStyle = "rgba(151, 229, 235, " + alpha.toFixed(3) + ")";
                context.lineWidth = progress < 0.35 ? 1.2 : 0.8;
                context.beginPath();
                context.moveTo(center + shimmer - segment, y);
                context.lineTo(center + shimmer + segment, y);
                context.stroke();
            }
            context.restore();
        }

        function drawSea(time) {
            var horizon = height * 0.51;
            var water = context.createLinearGradient(0, horizon, 0, height);
            water.addColorStop(0, "#103e50");
            water.addColorStop(0.32, "#0a3042");
            water.addColorStop(0.7, "#071f30");
            water.addColorStop(1, "#03121e");
            context.fillStyle = water;
            context.fillRect(0, horizon, width, height - horizon);

            drawReflection(time, horizon);

            var layers = [
                { base: horizon + 4, amplitude: 3.2, frequency: 0.012, speed: 0.45, phase: 0.1, fill: "rgba(31, 96, 112, 0.55)", stroke: "rgba(162, 230, 232, 0.20)", line: 0.8 },
                { base: horizon + height * 0.075, amplitude: 6, frequency: 0.0105, speed: -0.58, phase: 1.4, fill: "rgba(14, 68, 86, 0.72)", stroke: "rgba(151, 225, 228, 0.24)", line: 1 },
                { base: horizon + height * 0.17, amplitude: 9.5, frequency: 0.0092, speed: 0.74, phase: 2.1, fill: "rgba(8, 48, 66, 0.82)", stroke: "rgba(144, 220, 226, 0.30)", line: 1.1 },
                { base: horizon + height * 0.29, amplitude: 14, frequency: 0.008, speed: -0.92, phase: 0.8, fill: "rgba(5, 34, 51, 0.92)", stroke: "rgba(168, 232, 234, 0.36)", line: 1.3 },
                { base: horizon + height * 0.43, amplitude: 20, frequency: 0.0072, speed: 1.08, phase: 2.8, fill: "rgba(2, 20, 33, 0.98)", stroke: "rgba(182, 238, 238, 0.46)", line: 1.6 }
            ];

            layers.forEach(function (layer, layerIndex) {
                var path = traceWave(time, layer);
                var shape = new Path2D(path);
                shape.lineTo(width + 16, height + 20);
                shape.lineTo(-16, height + 20);
                shape.closePath();
                context.fillStyle = layer.fill;
                context.fill(shape);
                context.strokeStyle = layer.stroke;
                context.lineWidth = layer.line;
                context.stroke(path);

                if (layerIndex > 1) {
                    context.save();
                    context.setLineDash([3 + layerIndex * 2, 11 + layerIndex * 3]);
                    context.lineDashOffset = time * (layerIndex % 2 ? 9 : -7);
                    context.strokeStyle = "rgba(212, 247, 244, " + (0.09 + layerIndex * 0.035).toFixed(3) + ")";
                    context.lineWidth = 0.75 + layerIndex * 0.17;
                    context.stroke(path);
                    context.restore();
                }
            });

            var foreground = context.createLinearGradient(0, height * 0.76, 0, height);
            foreground.addColorStop(0, "rgba(1, 15, 26, 0)");
            foreground.addColorStop(1, "rgba(1, 9, 16, 0.74)");
            context.fillStyle = foreground;
            context.fillRect(0, height * 0.72, width, height * 0.28);
        }

        function draw(seconds) {
            context.clearRect(0, 0, width, height);
            drawSky(seconds);
            drawMoon(seconds);
            drawSea(seconds);
        }

        function tick(now) {
            if (!running) {
                return;
            }
            draw((now - start) / 1000);
            frame = requestAnimationFrame(tick);
        }

        function updatePlayback() {
            var shouldRun = visible && !reducedMotion.matches && !document.hidden;
            if (shouldRun && !running) {
                running = true;
                start = performance.now() - 4250;
                frame = requestAnimationFrame(tick);
            } else if (!shouldRun && running) {
                running = false;
                if (frame) {
                    cancelAnimationFrame(frame);
                }
                frame = null;
                draw(4.25);
            } else if (!shouldRun) {
                draw(4.25);
            }
        }

        function handlePointer(event) {
            var bounds = root.getBoundingClientRect();
            pointer.tx = ((event.clientX - bounds.left) / Math.max(1, bounds.width) - 0.5) * 2;
            pointer.ty = ((event.clientY - bounds.top) / Math.max(1, bounds.height) - 0.5) * 2;
        }

        root.addEventListener("pointermove", handlePointer, { passive: true });
        root.addEventListener("pointerleave", function () {
            pointer.tx = 0;
            pointer.ty = 0;
        }, { passive: true });

        if (window.ResizeObserver) {
            new ResizeObserver(resize).observe(root);
        } else {
            window.addEventListener("resize", resize, { passive: true });
        }

        if (window.IntersectionObserver) {
            new IntersectionObserver(function (entries) {
                visible = entries[0].isIntersecting;
                updatePlayback();
            }, { rootMargin: "160px 0px" }).observe(root);
        }

        document.addEventListener("visibilitychange", updatePlayback);
        if (reducedMotion.addEventListener) {
            reducedMotion.addEventListener("change", updatePlayback);
        } else if (reducedMotion.addListener) {
            reducedMotion.addListener(updatePlayback);
        }

        root.classList.add("deep-current-ocean-ready");
        resize();
        updatePlayback();
    }

    Array.prototype.forEach.call(oceans, createOcean);
}());
