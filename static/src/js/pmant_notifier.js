/** @odoo-module **/
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

const service = {
    dependencies: ["notification"],   // 👈 obligatorio para que esté en env.services
    start(env) {
        const notification = env.services.notification;  
        const seen = new Set();

        async function poll() {
            try {
                const res = await rpc("/pmant/notify/poll", {});
                if (Array.isArray(res) && res.length) {
                    const ids = [];
                    for (const n of res) {
                        if (seen.has(n.id)) continue;
                        seen.add(n.id);

                        notification.add(n.message, {
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
                console.warn("🕵️‍♂️ pmant_notifier: error while polling", e);
            } finally {
                setTimeout(poll, 60 * 1000);
            }
        }
        poll();
    },
};

registry.category("services").add("pmant_notifier", service);
