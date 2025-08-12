/** @odoo-module **/
import { registry } from "@web/core/registry";

const service = {
    start(env) {
        const rpc = env.services.rpc;
        const notify = env.services.notification;
        const seen = new Set();

        async function poll() {
            try {
                const res = await rpc("/pmant/notify/poll", {});
                if (Array.isArray(res) && res.length) {
                    const ids = [];
                    for (const n of res) {
                        if (seen.has(n.id)) continue;
                        seen.add(n.id);
                        notify.add(n.message, {
                            title: n.title || "Notificación",
                            type: n.type || "info",
                            sticky: !!n.sticky,
                        });
                        ids.push(n.id);
                    }
                    if (ids.length) {
                        await rpc("/pmant/notify/ack", { ids });
                    }
                }
            } catch (e) {
                // silenciar errores de red
            } finally {
                setTimeout(poll, 60 * 1000); // cada 60s
            }
        }
        poll();
    },
};

registry.category("services").add("pmant_notifier", service);
